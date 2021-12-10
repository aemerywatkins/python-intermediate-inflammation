"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np
from inflammation import serializers


def visualize(data_dict):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()


def display_patient_record(patient):
    """Display data for a single patient."""
    print(patient.name)
    for obs in patient.observations:
        print(obs.day, obs.value)


def display_patient_record_json(output_path, name):
    """Display patient record from stored JSON file"""
    records = serializers.PatientJSONSerializer.load(output_path)
    for i in records:
        if i.name == name:
            print(i.name)
            for obs in i.observations:
                print(obs.day, obs.value)
            return i
    print('Record for patient not found.')
    return None

