#!/usr/bin/env python3
"""Software for managing patient data in our imaginary hospital."""

import argparse

from inflammation import models, views


def main(args):
    """The MVC Controller of the patient data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles
    if infiles != None:
        if not isinstance(infiles, list):
            infiles = [args.infiles]

        for filename in infiles:
            inflammation_data = models.load_csv(filename)

            if args.view == 'visualize':
                view_data = {
                    'average': models.daily_mean(inflammation_data),
                    'max': models.daily_max(inflammation_data),
                    'min': models.daily_min(inflammation_data),
                }

                views.visualize(view_data)

            elif args.view == 'record':
                patient_data = inflammation_data[args.patient]
                observations = [models.Observation(day, value) for day, value in enumerate(patient_data)]
                patient = models.Patient('UNKNOWN', observations)

                views.display_patient_record(patient)

    elif (args.json_path != None) & (args.patient_name != None):
        try:
            views.display_patient_record_json(args.json_path, args.patient_name)
        except:
            print('Either the path or the patient name is wrong.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient data management system')

    parser.add_argument(
        '--infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        '--view',
        default='visualize',
        choices=['visualize', 'record'],
        help='Which view should be used?')

    parser.add_argument(
        '--patient',
        type=int,
        default=0,
        help='Which patient should be displayed?')

    parser.add_argument(
        '--json_path',
        type=str,
        default='tests/patient.json',
        help='Provide path to specific patient file (.json)',
    )

    parser.add_argument(
        '--patient_name',
        type=str,
        default=None,
        help='Provide the patient name, e.g., Alice'
    )

    args = parser.parse_args()

    main(args)
