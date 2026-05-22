"""SAQA 118792 AI Software Developer (NQF 5)
Lesson 09 - Deep Learning with Python and TensorFlow

Covers:
  KM-09 Deep Learning (NQF5, 16 cr)
  PM-08 Demonstrate ability to build a DL Neural Network in Python (NQF5, 10 cr)
  PM-09 Demonstrate ability to build a DL Neural Network in TensorFlow (NQF5, 10 cr)
"""

LESSON_HTML = (
    "<h2>Deep Learning with Python and TensorFlow</h2>"
    "<p>Deep learning is the branch of machine learning that uses <strong>multi-layer "
    "artificial neural networks</strong> to learn hierarchical representations directly "
    "from raw data such as pixels, audio samples, or token sequences. It now powers "
    "image recognition, speech, machine translation, recommender systems, and the large "
    "language models behind modern AI assistants. In this lesson we trace the path from "
    "the single <em>perceptron</em> all the way to convolutional, recurrent and "
    "transformer architectures, and we build a working network in <strong>TensorFlow / "
    "Keras</strong>.</p>"

    "<h3>From perceptron to multi-layer perceptron (MLP)</h3>"
    "<p>A perceptron computes <code>y = step(w&middot;x + b)</code>. A single perceptron "
    "can only separate <em>linearly separable</em> data, so it famously cannot learn the "
    "XOR function. Stacking many neurons into <strong>hidden layers</strong> with "
    "<em>non-linear</em> activations produces a multi-layer perceptron, which is a "
    "universal function approximator: given enough hidden units it can approximate any "
    "continuous mapping from inputs to outputs.</p>"

    "<h3>Forward and backward propagation</h3>"
    "<p><strong>Forward propagation</strong> pushes the input through each layer, "
    "computing weighted sums and activations, until a prediction emerges. A "
    "<strong>loss function</strong> measures how wrong that prediction is. "
    "<strong>Backward propagation</strong> (the chain rule applied layer-by-layer) "
    "computes the gradient of the loss with respect to every weight and bias, so an "
    "optimiser can nudge the parameters in the direction that reduces the loss.</p>"

    "<h3>Gradient descent variants</h3>"
    "<ul>"
    "<li><strong>Batch GD</strong> &mdash; uses the whole dataset per update; accurate "
    "but slow and memory-heavy.</li>"
    "<li><strong>SGD</strong> (Stochastic) &mdash; one sample per update; noisy but fast "
    "and can escape shallow minima.</li>"
    "<li><strong>Mini-batch SGD</strong> &mdash; updates from small batches (typically "
    "32&ndash;256); the practical default.</li>"
    "<li><strong>Momentum</strong> &mdash; adds a velocity term so updates accelerate "
    "down consistent slopes.</li>"
    "<li><strong>RMSProp</strong> &mdash; scales each parameter's learning rate by a "
    "running average of squared gradients.</li>"
    "<li><strong>Adam</strong> &mdash; combines momentum and RMSProp; the most popular "
    "default optimiser for deep nets.</li>"
    "</ul>"

    "<h3>Activation functions &mdash; where and why</h3>"
    "<table><thead><tr><th>Activation</th><th>Range</th><th>Typical use</th></tr>"
    "</thead><tbody>"
    "<tr><td>Sigmoid</td><td>(0, 1)</td><td>Binary output layer; rarely in hidden "
    "layers due to vanishing gradients.</td></tr>"
    "<tr><td>Tanh</td><td>(-1, 1)</td><td>Zero-centred alternative to sigmoid; still "
    "saturates.</td></tr>"
    "<tr><td>ReLU</td><td>[0, &infin;)</td><td>Default hidden-layer activation; cheap "
    "and avoids vanishing gradients.</td></tr>"
    "<tr><td>Leaky ReLU</td><td>(-&infin;, &infin;)</td><td>Fixes the &quot;dying "
    "ReLU&quot; problem with a small negative slope.</td></tr>"
    "<tr><td>Softmax</td><td>(0, 1) summing to 1</td><td>Multi-class output layer; "
    "produces a probability distribution.</td></tr>"
    "</tbody></table>"

    "<h3>Loss functions</h3>"
    "<ul>"
    "<li><strong>MSE</strong> (mean squared error) for regression.</li>"
    "<li><strong>Binary cross-entropy</strong> for two-class problems with a sigmoid "
    "output.</li>"
    "<li><strong>Categorical / sparse categorical cross-entropy</strong> for "
    "multi-class problems with a softmax output.</li>"
    "</ul>"

    "<h3>Weight initialisation</h3>"
    "<p>Poor initialisation kills training. <strong>Xavier (Glorot)</strong> "
    "initialisation suits tanh/sigmoid; <strong>He</strong> initialisation suits ReLU. "
    "Both scale the random weights by the layer size so signals neither explode nor "
    "vanish as they propagate.</p>"

    "<h3>Regularisation</h3>"
    "<ul>"
    "<li><strong>L1 / L2</strong> penalties on the weights discourage over-large "
    "parameters.</li>"
    "<li><strong>Dropout</strong> randomly zeroes a fraction of activations during "
    "training so the network cannot rely on any one neuron.</li>"
    "<li><strong>Batch normalisation</strong> standardises layer inputs, stabilising "
    "and accelerating training.</li>"
    "<li><strong>Early stopping</strong> halts training when validation loss stops "
    "improving.</li>"
    "<li><strong>Data augmentation</strong> (flips, crops, noise) cheaply enlarges the "
    "training set and improves generalisation.</li>"
    "</ul>"

    "<h3>Convolutional Neural Networks (CNNs)</h3>"
    "<p>CNNs exploit spatial structure in images. Core building blocks:</p>"
    "<ul>"
    "<li><strong>Convolution</strong> &mdash; a small learned filter slides across the "
    "image producing a <em>feature map</em> that highlights edges, textures, shapes.</li>"
    "<li><strong>Stride</strong> &mdash; how far the filter jumps each step.</li>"
    "<li><strong>Padding</strong> &mdash; adding a border of zeros so output size is "
    "preserved (<code>same</code>) or shrinks (<code>valid</code>).</li>"
    "<li><strong>Pooling</strong> (max / average) &mdash; downsamples feature maps, "
    "giving translation invariance.</li>"
    "</ul>"
    "<p>Famous architectures: <strong>LeNet-5</strong> (digits, 1998), <strong>VGG</strong> "
    "(deep stacks of 3&times;3 convs, 2014), <strong>ResNet</strong> (residual / skip "
    "connections that allow training of 50- to 152-layer networks without vanishing "
    "gradients).</p>"

    "<h3>Recurrent networks for sequences</h3>"
    "<p>Plain <strong>RNNs</strong> keep a hidden state that is updated at each time "
    "step, but suffer from vanishing gradients on long sequences. <strong>LSTM</strong> "
    "and <strong>GRU</strong> cells add gating mechanisms (input/forget/output gates) "
    "that let information flow across hundreds of time steps, making them suitable for "
    "language, time-series and audio.</p>"

    "<h3>Transformers and attention</h3>"
    "<p>A <strong>self-attention</strong> layer lets every token in a sequence look at "
    "every other token and compute a weighted summary, with no recurrence. Stacking "
    "many attention + feed-forward blocks gives the <strong>Transformer</strong> "
    "architecture that underlies BERT, GPT and most modern LLMs. Transformers train "
    "well on GPUs/TPUs because the attention computation is highly parallel.</p>"

    "<h3>Transfer learning</h3>"
    "<p>Instead of training a giant network from scratch, you download weights from a "
    "model pre-trained on a huge dataset (ImageNet, large text corpora), freeze most "
    "layers, and fine-tune the final layers on your own (often small) dataset. This is "
    "the standard recipe for production computer-vision and NLP systems.</p>"

    "<h3>TensorFlow and the Keras API</h3>"
    "<p><strong>TensorFlow</strong> is an open-source numerical computing library that "
    "executes computation graphs on CPU, GPU or TPU. <strong>Keras</strong> is its "
    "high-level Python API and offers three levels of abstraction:</p>"
    "<ol>"
    "<li><strong>Sequential</strong> &mdash; a simple linear stack of layers.</li>"
    "<li><strong>Functional</strong> &mdash; a graph of layers supporting multiple "
    "inputs/outputs and shared layers.</li>"
    "<li><strong>Subclassing</strong> &mdash; write a Python class extending "
    "<code>tf.keras.Model</code> for full flexibility.</li>"
    "</ol>"

    "<h3>A minimal Keras Sequential model (MNIST-style)</h3>"
    "<pre><code>import tensorflow as tf\n"
    "from tensorflow.keras import layers, models\n"
    "\n"
    "(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()\n"
    "x_train, x_test = x_train / 255.0, x_test / 255.0\n"
    "\n"
    "model = models.Sequential([\n"
    "    layers.Flatten(input_shape=(28, 28)),\n"
    "    layers.Dense(128, activation='relu'),\n"
    "    layers.Dropout(0.2),\n"
    "    layers.Dense(10, activation='softmax'),\n"
    "])\n"
    "\n"
    "model.compile(optimizer='adam',\n"
    "              loss='sparse_categorical_crossentropy',\n"
    "              metrics=['accuracy'])\n"
    "model.fit(x_train, y_train, epochs=5, validation_split=0.1)\n"
    "loss, acc = model.evaluate(x_test, y_test)\n"
    "print('Test accuracy:', acc)\n"
    "</code></pre>"

    "<h3>A small CNN with the Functional API</h3>"
    "<pre><code>inputs = tf.keras.Input(shape=(28, 28, 1))\n"
    "x = layers.Conv2D(32, 3, activation='relu', padding='same')(inputs)\n"
    "x = layers.MaxPooling2D()(x)\n"
    "x = layers.Conv2D(64, 3, activation='relu', padding='same')(x)\n"
    "x = layers.MaxPooling2D()(x)\n"
    "x = layers.Flatten()(x)\n"
    "x = layers.Dense(64, activation='relu')(x)\n"
    "outputs = layers.Dense(10, activation='softmax')(x)\n"
    "cnn = tf.keras.Model(inputs, outputs)\n"
    "cnn.compile(optimizer='adam',\n"
    "            loss='sparse_categorical_crossentropy',\n"
    "            metrics=['accuracy'])\n"
    "</code></pre>"

    "<h3>tf.data input pipelines</h3>"
    "<p><code>tf.data.Dataset</code> builds efficient, GPU-friendly input pipelines "
    "with <code>.shuffle()</code>, <code>.batch()</code>, <code>.map()</code> and "
    "<code>.prefetch(tf.data.AUTOTUNE)</code>, overlapping data preparation with "
    "training so the accelerator is never idle.</p>"
    "<pre><code>ds = tf.data.Dataset.from_tensor_slices((x_train, y_train))\n"
    "ds = ds.shuffle(10000).batch(64).prefetch(tf.data.AUTOTUNE)\n"
    "model.fit(ds, epochs=5)\n"
    "</code></pre>"

    "<h3>GPU acceleration and saving models</h3>"
    "<p>If a CUDA-enabled GPU is visible, TensorFlow uses it automatically; check with "
    "<code>tf.config.list_physical_devices('GPU')</code>. Models can be persisted as:"
    "</p>"
    "<ul>"
    "<li><strong>SavedModel</strong> (<code>model.save('path')</code>) &mdash; the "
    "recommended portable format that bundles the graph, weights and signatures.</li>"
    "<li><strong>HDF5</strong> (<code>model.save('model.h5')</code>) &mdash; a single "
    "file, convenient but legacy.</li>"
    "</ul>"
    "<p>Reload either with <code>tf.keras.models.load_model(path)</code>.</p>"

    "<h3>Ethical concerns of large models</h3>"
    "<blockquote>Large deep-learning models can memorise and amplify bias in their "
    "training data, consume enormous energy, enable convincing deepfakes and "
    "disinformation, and concentrate power in a few well-resourced organisations. "
    "Responsible practice means measuring bias across demographic groups, documenting "
    "datasets and model cards, respecting copyright and consent, reporting carbon "
    "cost, and adding human-in-the-loop checks for high-stakes decisions.</blockquote>"
)


QUESTIONS = [
    (
        "mc",
        "<p>Which activation function is the standard default for the hidden layers of"
        " a modern deep neural network because it is cheap to compute and largely"
        " avoids the vanishing-gradient problem?</p>",
        [
            ("<p>Sigmoid</p>", False),
            ("<p>Tanh</p>", False),
            ("<p>ReLU</p>", True),
            ("<p>Softmax</p>", False),
        ],
        "<p>ReLU (<code>max(0, x)</code>) is the default hidden-layer activation."
        " Sigmoid and tanh saturate and cause vanishing gradients; softmax is used at"
        " the output layer of multi-class classifiers.</p>",
    ),
    (
        "mc",
        "<p>You are building the <em>output layer</em> of a network that must classify"
        " an image into one of 10 mutually exclusive digit classes. Which combination"
        " of output activation and loss is most appropriate?</p>",
        [
            ("<p>Sigmoid output + binary cross-entropy</p>", False),
            ("<p>Softmax output + categorical (or sparse categorical) cross-entropy"
             "</p>", True),
            ("<p>ReLU output + mean squared error</p>", False),
            ("<p>Tanh output + hinge loss</p>", False),
        ],
        "<p>Multi-class classification with mutually exclusive labels uses a softmax"
        " output (a probability distribution over classes) paired with categorical or"
        " sparse categorical cross-entropy.</p>",
    ),
    (
        "mc",
        "<p>What is the primary purpose of a <strong>Dropout</strong> layer during"
        " training?</p>",
        [
            ("<p>To speed up matrix multiplication on the GPU.</p>", False),
            ("<p>To normalise the inputs of each mini-batch to zero mean and unit"
             " variance.</p>", False),
            ("<p>To randomly deactivate a fraction of neurons so the network cannot"
             " rely on any single unit, reducing overfitting.</p>", True),
            ("<p>To replace the activation function in the output layer.</p>", False),
        ],
        "<p>Dropout randomly zeroes a fraction of activations during training, forcing"
        " the network to learn redundant, more robust features and reducing"
        " overfitting. Batch normalisation is what standardises layer inputs.</p>",
    ),
    (
        "mc",
        "<p>Which optimiser combines <em>momentum</em> with <em>per-parameter adaptive"
        " learning rates</em> based on a running average of squared gradients, and is"
        " a common default for deep networks?</p>",
        [
            ("<p>Vanilla SGD</p>", False),
            ("<p>Adam</p>", True),
            ("<p>Batch gradient descent</p>", False),
            ("<p>Newton's method</p>", False),
        ],
        "<p>Adam (Adaptive Moment Estimation) merges momentum (first moment of the"
        " gradient) with RMSProp-style per-parameter learning rates (second moment),"
        " and is the most widely used default optimiser.</p>",
    ),
    (
        "mc",
        "<p>In a convolutional layer, what is a <strong>feature map</strong>?</p>",
        [
            ("<p>A lookup table that maps class indices to human-readable labels.</p>",
             False),
            ("<p>The 2D output produced by sliding one learned filter (kernel) across"
             " the input, highlighting where that filter's pattern occurs.</p>", True),
            ("<p>The list of hyperparameters used to configure the optimiser.</p>",
             False),
            ("<p>A diagram of the layers and tensor shapes of the network.</p>", False),
        ],
        "<p>Each convolutional filter produces one feature map &mdash; a 2D activation"
        " grid that responds strongly wherever the filter's learned pattern (edge,"
        " texture, shape) appears in the input.</p>",
    ),
    (
        "mc",
        "<p>Which Keras API level is best described as &quot;a graph of layers that"
        " supports multiple inputs, multiple outputs, and shared layers&quot;?</p>",
        [
            ("<p>Sequential API</p>", False),
            ("<p>Functional API</p>", True),
            ("<p>Model Subclassing API</p>", False),
            ("<p>Estimator API</p>", False),
        ],
        "<p>The Functional API expresses a model as a directed graph of layers and is"
        " required whenever you need branching, multiple inputs/outputs or shared"
        " layers. Sequential is limited to a linear stack; subclassing gives full"
        " imperative flexibility.</p>",
    ),
    (
        "tf",
        "<p>True or false: A single-layer perceptron with a step activation can learn"
        " the XOR function.</p>",
        [
            ("<p>True</p>", False),
            ("<p>False</p>", True),
        ],
        "<p>False. XOR is not linearly separable, so a single perceptron cannot learn"
        " it. At least one hidden layer with a non-linear activation is required.</p>",
    ),
    (
        "tf",
        "<p>True or false: In TensorFlow / Keras, calling <code>model.save('my_model')"
        "</code> with no file extension produces a <em>SavedModel</em> directory that"
        " bundles the architecture, weights and signatures, and can be reloaded with"
        " <code>tf.keras.models.load_model('my_model')</code>.</p>",
        [
            ("<p>True</p>", True),
            ("<p>False</p>", False),
        ],
        "<p>True. The SavedModel format is the recommended portable format. Passing a"
        " <code>.h5</code> filename instead produces a single HDF5 file (legacy"
        " format).</p>",
    ),
]


PRACTICAL_HTML = (
    "<h2>Practical Lab \u2014 Train a Neural Network on MNIST in Keras</h2>"
    "<p>In this lab you will train, evaluate, visualise and persist a small neural"
    " network that classifies hand-written digits from the classic <strong>MNIST"
    "</strong> dataset. By the end you should reach roughly <strong>97% test"
    " accuracy</strong> in under a minute on a CPU.</p>"

    "<h3>1. Set up the environment</h3>"
    "<p>Install TensorFlow (it brings Keras with it) and Matplotlib:</p>"
    "<pre><code>pip install tensorflow matplotlib\n"
    "</code></pre>"
    "<p>Confirm the install and check for a GPU:</p>"
    "<pre><code>import tensorflow as tf\n"
    "print('TF version:', tf.__version__)\n"
    "print('GPUs:', tf.config.list_physical_devices('GPU'))\n"
    "</code></pre>"

    "<h3>2. Load and inspect MNIST</h3>"
    "<pre><code>(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()\n"
    "print(x_train.shape, y_train.shape)   # (60000, 28, 28) (60000,)\n"
    "print(x_test.shape,  y_test.shape)    # (10000, 28, 28) (10000,)\n"
    "print('Pixel range:', x_train.min(), x_train.max())  # 0 255\n"
    "</code></pre>"

    "<h3>3. Normalise the pixels to the 0\u20131 range</h3>"
    "<p>Neural networks train much better when inputs are small floats centred near"
    " zero. Dividing by 255 maps each pixel into <code>[0.0, 1.0]</code>.</p>"
    "<pre><code>x_train = x_train.astype('float32') / 255.0\n"
    "x_test  = x_test.astype('float32')  / 255.0\n"
    "</code></pre>"

    "<h3>4. Build the model (Sequential MLP)</h3>"
    "<pre><code>from tensorflow.keras import layers, models\n"
    "\n"
    "model = models.Sequential([\n"
    "    layers.Flatten(input_shape=(28, 28)),     # 784-d vector\n"
    "    layers.Dense(128, activation='relu'),     # hidden layer\n"
    "    layers.Dropout(0.2),                      # regularisation\n"
    "    layers.Dense(10,  activation='softmax'),  # 10-class output\n"
    "])\n"
    "model.summary()\n"
    "</code></pre>"

    "<h3>5. Compile</h3>"
    "<pre><code>model.compile(\n"
    "    optimizer='adam',\n"
    "    loss='sparse_categorical_crossentropy',\n"
    "    metrics=['accuracy'],\n"
    ")\n"
    "</code></pre>"
    "<p>We use <code>sparse_categorical_crossentropy</code> because the labels are"
    " integers 0\u20139 (not one-hot vectors).</p>"

    "<h3>6. Fit for 5 epochs with a validation split</h3>"
    "<pre><code>history = model.fit(\n"
    "    x_train, y_train,\n"
    "    epochs=5,\n"
    "    validation_split=0.1,\n"
    "    verbose=2,\n"
    ")\n"
    "</code></pre>"

    "<h3>7. Evaluate on the held-out test set</h3>"
    "<pre><code>test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)\n"
    "print('Test loss:    ', round(test_loss, 4))\n"
    "print('Test accuracy:', round(test_acc, 4))\n"
    "</code></pre>"

    "<h3>Expected output (yours will be similar)</h3>"
    "<pre><code>Epoch 1/5 - loss: 0.2949 - accuracy: 0.9148 - val_loss: 0.1466 - val_accuracy: 0.9580\n"
    "Epoch 2/5 - loss: 0.1426 - accuracy: 0.9576 - val_loss: 0.1062 - val_accuracy: 0.9692\n"
    "Epoch 3/5 - loss: 0.1066 - accuracy: 0.9676 - val_loss: 0.0915 - val_accuracy: 0.9732\n"
    "Epoch 4/5 - loss: 0.0876 - accuracy: 0.9729 - val_loss: 0.0855 - val_accuracy: 0.9748\n"
    "Epoch 5/5 - loss: 0.0744 - accuracy: 0.9766 - val_loss: 0.0808 - val_accuracy: 0.9763\n"
    "Test loss:     0.0731\n"
    "Test accuracy: 0.9773\n"
    "</code></pre>"

    "<h3>8. Plot training vs validation loss</h3>"
    "<pre><code>import matplotlib.pyplot as plt\n"
    "\n"
    "plt.plot(history.history['loss'],     label='train loss')\n"
    "plt.plot(history.history['val_loss'], label='val loss')\n"
    "plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.legend()\n"
    "plt.title('MNIST MLP - training vs validation loss')\n"
    "plt.show()\n"
    "</code></pre>"
    "<p>If the validation curve starts rising while the training curve keeps falling,"
    " the model is <em>overfitting</em> &mdash; consider more dropout, smaller layers,"
    " or early stopping.</p>"

    "<h3>9. Predict on 5 random test images</h3>"
    "<pre><code>import numpy as np\n"
    "\n"
    "idx = np.random.choice(len(x_test), 5, replace=False)\n"
    "probs = model.predict(x_test[idx])\n"
    "preds = probs.argmax(axis=1)\n"
    "\n"
    "fig, axes = plt.subplots(1, 5, figsize=(10, 2))\n"
    "for ax, image, pred, true in zip(axes, x_test[idx], preds, y_test[idx]):\n"
    "    ax.imshow(image, cmap='gray')\n"
    "    ax.set_title('pred ' + str(pred) + ' / true ' + str(true))\n"
    "    ax.axis('off')\n"
    "plt.show()\n"
    "</code></pre>"

    "<h3>10. Save and reload the model</h3>"
    "<pre><code># Recommended portable SavedModel format (a directory):\n"
    "model.save('mnist_mlp')\n"
    "\n"
    "# Or single-file HDF5:\n"
    "model.save('mnist_mlp.h5')\n"
    "\n"
    "# Reload and confirm it still works:\n"
    "reloaded = tf.keras.models.load_model('mnist_mlp')\n"
    "_, acc = reloaded.evaluate(x_test, y_test, verbose=0)\n"
    "print('Reloaded test accuracy:', round(acc, 4))\n"
    "</code></pre>"

    "<h3>Reflection questions</h3>"
    "<ol>"
    "<li>Your training accuracy climbs above 98% while validation accuracy stalls"
    " around 97.5%. Which regularisation techniques from the lesson would you try"
    " <em>first</em>, and why?</li>"
    "<li>You change the loss from <code>sparse_categorical_crossentropy</code> to"
    " <code>mean_squared_error</code> and accuracy drops noticeably. Explain why MSE"
    " is a poor choice for this 10-class softmax classifier.</li>"
    "<li>Replace the MLP with a small CNN (two <code>Conv2D</code>+<code>MaxPooling2D"
    "</code> blocks, then <code>Flatten</code> + <code>Dense(10, softmax)</code>) and"
    " retrain for the same 5 epochs. Compare the test accuracy, the number of"
    " parameters reported by <code>model.summary()</code>, and the training time. Why"
    " does a CNN typically reach higher accuracy on image data than an MLP with a"
    " similar parameter count?</li>"
    "</ol>"
)


assert LESSON_HTML.startswith("<h2>Deep Learning with Python and TensorFlow</h2>")
assert len(LESSON_HTML) >= 2400, len(LESSON_HTML)
assert PRACTICAL_HTML.startswith(
    "<h2>Practical Lab \u2014 Train a Neural Network on MNIST in Keras</h2>"
)
assert len(PRACTICAL_HTML) >= 1800, len(PRACTICAL_HTML)
assert len(QUESTIONS) == 8
_mc = sum(1 for q in QUESTIONS if q[0] == "mc")
_tf = sum(1 for q in QUESTIONS if q[0] == "tf")
assert _mc >= 6 and _tf <= 2 and _mc + _tf == 8
for _qtype, _qhtml, _opts, _fb in QUESTIONS:
    assert _qtype in ("mc", "tf")
    assert len(_opts) == (4 if _qtype == "mc" else 2)
    assert sum(1 for _, _ok in _opts if _ok) == 1
