import pandas as pd
import tensorflow
import tensorflow.keras as keras
import tensorflow.keras.layers as layers
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def main():
    covid_world = pd.read_csv('owid-covid-data.csv')

    # Get a random dataframe
    covid_us = covid_world.loc[covid_world['location'] == 'United States', :].sample(frac=1)

    # convert date string to numberical values
    covid_us['date'] = covid_us['date'].apply(
        lambda d: datetime.strptime(d, '%Y-%m-%d').timestamp()
    )

    # splite data
    data, targets = covid_us['date'], covid_us['new_cases']
    train_data, train_targets = data[:8], targets[:8]
    test_data, test_targets = data[8:], targets[8:]

    # set up normalizer
    normalizer = keras.layers.experimental.preprocessing.Normalization()
    normalizer.adapt(np.array(train_data))

    # build the model
    model = keras.models.Sequential([
        normalizer,
        layers.Dense(32, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(16),
        layers.Dense(1)
    ])
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.01),
        loss='mean_absolute_error',
    )
    history = model.fit(
        train_data, train_targets,
        validation_split=0.2,
        epochs=30, batch_size=1, verbose=0)

    # plot history
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Validation loss')
    plt.legend()
    plt.show()

    # evaluate result
    result = model.evaluate(test_data, test_targets)
    print(result)
    print(model.predict([datetime.now().timestamp()]))


if __name__ == '__main__':
    main()
