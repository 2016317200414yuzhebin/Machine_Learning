import numpy as np
from features import prepare_for_training
from hypothesis import sigmoid, sigmoid_gradient

class MultilayerPerceptron:
    def __init__(self, data, labels, layers, normalize_data = False):
        data_processed = prepare_for_training(data, normalize_data = normalize_data)
        self.data = data_processed
        self.labels = labels
        self.layers = layers
        self.normalize_data = normalize_data
        self.thetas = MultilayerPerceptron.thetas_init(layers)

    @staticmethod
    def thetas_init(layers):
        num_layers = len(layers)
        thetas = dict()

        # Execute twice to get two sets of parameter matrices
        # 25 * 785, 10 * (25 + 1)
        for layer_index in range(num_layers - 1):
            in_count = layers[layer_index]
            out_count =  layers[layer_index + 1]
            # Initialize weight matrix and bias term (+1)
            thetas[layer_index] = np.random.rand(out_count, in_count + 1) * 0.05
        
        return thetas

    @staticmethod
    def thetas_unroll(thetas):
        num_theta_layers = len(thetas)
        unrolled_theta = np.array()
        for theta_layer_index in range(num_theta_layers):
            unrolled_theta = np.hstack(unrolled_theta, thetas[theta_layer_index].flatten())
        return unrolled_theta

    @staticmethod
    def thetas_roll(unrolled_thetas, layers):
        num_layers = len(layers)
        thetas = dict()
        unrolled_shift = 0
        for layer_index in range(num_layers - 1):
            in_count = layers[layer_index]
            out_count =  layers[layer_index + 1]
            thetas_width = in_count + 1
            thetas_height = out_count
            thetas_volume = thetas_width * thetas_height
            start_index = unrolled_shift
            end_index = unrolled_shift + thetas_volume
            layer_theta_unrolled = unrolled_thetas[start_index:end_index]
            thetas[layer_index] = layer_theta_unrolled.reshape((thetas_height, thetas_width))
            unrolled_shift += thetas_volume
        
        return thetas
    
    def train(self, max_interation = 1000, alpha = 0.1):
        unrolled_theta = MultilayerPerceptron.thetas_unroll(self.thetas)
        (optimized_theta, cost_history) = MultilayerPerceptron.gradient_descent(self.data, self.labels, unrolled_theta, self.layers, max_interation, alpha)
        self.thetas = MultilayerPerceptron.thetas_roll(optimized_theta, self.layers)
        return self.thetas, cost_history

    @staticmethod
    def gradient_descent(data, labels, unrolled_theta, layers, max_interation, alpha):
        optimized_theta = unrolled_theta
        cost_history = []
        rolled_theta = MultilayerPerceptron.thetas_roll(unrolled_theta, layers)
        for _ in range(max_interation):
            cost = MultilayerPerceptron.cost_function(data, labels, rolled_theta, layers)
            cost_history.append(cost)
            theta_gradient = MultilayerPerceptron.gradient_step(data, labels, optimized_theta, layers)
            optimized_theta = optimized_theta - alpha * theta_gradient
        return optimized_theta, cost_history

    @staticmethod
    def cost_function(data, labels, thetas, layers):
        num_layers = len(layers)
        num_examples = data.shape[0]
        num_labels = layers[-1]
        
        # Do a feedforward
        predictions = MultilayerPerceptron.feedforward_propagation(data, thetas, layers)
        
        # Make labels, each label is one-hot
        bitwise_labels = np.zeros((num_examples, num_labels))
        for example_index in range(num_examples):
            bitwise_labels[example_index][labels[example_index][0]] = 1
        bit_set_cost = np.sum(np.log(predictions[bitwise_labels == 1]))
        bit_not_set_cost = np.sum(np.log(1 - predictions[bitwise_labels == 0]))
        cost = (-1 / num_examples) * (bit_set_cost + bit_not_set_cost)
        return  cost

    @staticmethod
    def gradient_step(data, labels, optimized_theta, layers):
        theta = MultilayerPerceptron.thetas_roll(optimized_theta)
        thetas_rolled_gradients = MultilayerPerceptron.back_propagation(data, labels, theta, layers)
        thetas_unrolled_gradients = MultilayerPerceptron.thetas_unroll(thetas_rolled_gradients)
        return thetas_unrolled_gradients

    @staticmethod
    def feedforward_propagation(data, thetas, layers):
        num_layers = len(layers)
        num_examples = data.shape[0]
        in_layer_activation = data

        # Calculation layer by layer
        for layer_index in range(num_layers - 1):
            theta = thetas[layer_index]
            out_layer_activation = sigmoid(np.dot(in_layer_activation, theta.T))
            # After calculation, it is num_example * 25, but the bias item must be considered.
            out_layer_activation = np.hstack((np.ones((num_examples, 1)), out_layer_activation))
            in_layer_activation = out_layer_activation

        # return output layer result
        return in_layer_activation[:, 1:]

    @staticmethod
    def back_propagation(data, labels, thetas, layers):
        num_layers = len(layers)
        (num_examples, num_features) = data.shape
        num_label_types = layers[-1]
        deltas = dict()

        for layer_index in range(num_layers - 1):
            in_count = layers[layer_index]
            out_count = layers[layer_index + 1]
            # 25 * 785, 10 * 26
            deltas[layer_index] = np.zeros((out_count, in_count + 1))
        
        for example_index in range(num_examples):
            layers_inputs = dict()
            layers_activations = dict()
            # 785 * 1
            layers_activation = data[example_index, :].reshape((num_features, 1))
            layers_activations[0] = layers_activation
            # Calculation layer by layer
            for layer_index in range(num_layers - 1):
                # Current weight parameter value 25 * 785  10 * 26
                layer_theta = thetas[layer_index]
                # Get 25 * 1 for the first time, 10 * 1 for the second time
                layer_input = np.dot(layer_theta, layers_activation)
                layers_activation = np.vstack((np.array([[1]]), sigmoid(layer_input)))
                # The calculation result of the next layer
                layers_inputs[layer_index + 1] = layer_input
                # The result of the next layer after the activation function
                layers_activations[layer_index + 1] = layers_activation
            output_layer_activation = layers_activations[1:, :]
            
            delta = dict()
            # label processing
            bitwise_label = np.zeros((num_label_types, 1))
            bitwise_label[labels[example_index][0]] = 1
            # Calculate the difference between the output layer and the ground truth
            delta[num_layers - 1] = output_layer_activation - bitwise_label

            # Loop through L, L-1, L-2, ..., 2
            for layer_index in range(num_layers - 2, 0, -1):
                layer_theta = thetas[layer_index]
                next_delta = delta[layer_index + 1]
                layer_input = layers_inputs[layer_index]
                layer_input = np.vstack(np.array((1)), layer_input)
                delta[layer_index] = np.dot(layer_theta.T, next_delta) * sigmoid_gradient(layer_input)
                delta[layer_index] = delta[layer_index][1:, :]
            
            for layer_index in range(num_layers - 1):
                layer_delta = np.dot(delta[layer_index + 1], layers_activations[layer_index].T)
                # fisrt time 25 * 785, second time 10 * 26
                deltas[layer_index] += layer_delta
            
            for layer_index in range(num_layers - 1):
                deltas[layer_index] = deltas[layer_index] * (1 / num_examples)

            return deltas