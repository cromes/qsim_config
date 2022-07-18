class config(object):
    """
    scriptscanner config object for the molecules experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'Qsim.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [
        (exps + 'Interleaved_Linescan.interleaved_linescan', 'interleaved_linescan'),

        (exps + 'Line_Narrowing.line_narrowing', 'line_narrowing'),

        (exps + 'Randomized_Benchmarking.randomized_benchmarking', 'RandomizedBenchmarking'),

        # (exps + 'off_resonant_shelving_measurement.off_resonant_shelving_measurement', 'off_resonant_shelving_measurement'),

        (exps + 'Bright_State_Detection.bright_state_detection', 'BrightStateDetection'),

        (exps + 'Dark_State_Detection.dark_state_detection', 'DarkStateDetection'),

        (exps + 'SF_Discrimination_Experiment.sf_discrimination_experiment', 'sf_discrimination_experiment'),

        (exps + 'Coherence_Measurement.coherence_measurement', 'coherence_measurement'),

        (exps + 'FFT.PMT_FFT', 'PMT_FFT'),

        # (exps + 'tickle.tickle_experiment', 'ticklescan'),

        (exps + 'Laser_Frequency_Tracker.laser_frequency_tracker',
         'laser_frequency_tracker'),

        (exps + 'Optical_Pumping_Rate.optical_pumping_rate',
         'optical_pumping_rate'),

        ( exps + 'Quadrupole_Optical_Pumping_Linescan.quadrupole_optical_pumping_linescan',
        'quadrupole_optical_pumping_linescan'),

        (exps + 'Fidelity_Tweak_Up.fidelity_tweak_up',
         'fidelity_tweak_up'),

        (exps + 'Microwave_Rabi_Flopping.microwave_rabi_flopping', 'MicrowaveRabiFlopping'),

        (exps + 'Microwave_Linescan.microwave_linescan', 'MicrowaveLineScan'),

        (exps + 'Microwave_Linescan.microwave_linescan_minus', 'MicrowaveLineScanMinus'),

        (exps + 'Microwave_Linescan.microwave_linescan_plus', 'MicrowaveLineScanPlus'),

        (exps + 'Microwave_Rabi_Flopping.microwave_rabi_flopping_clock', 'MicrowaveRabiFloppingClock'),

        (exps + 'Quadrupole_Linescan.quadrupole_linescan',
         'QuadrupoleLineScan'),

        (exps + 'Quadrupole_Rabi_Flopping.quadrupole_rabi_flopping',
         'QuadrupoleRabiFlopping'),

        (exps + 'Microwave_Ramsey_Experiment.microwave_ramsey_experiment', 'MicrowaveRamseyExperiment'),

        (exps + 'High_Fidelity_Dark_State_SPAM.High_Fidelity_Dark_State_SPAM', 'high_fidelity_dark_state_spam'),

        (exps + 'DAC_Raster.DAC_Raster', 'dacRaster'),

        (exps + 'Shelving_Rate.shelving_rate', 'shelving_rate'),

        (exps + 'Deshelving_Rate.deshelving_rate', 'deshelving_rate'),

        (exps + 'Wavemeter_Linescan.wavemeter_linescan', 'wavemeter_linescan'),

        (exps + 'Metastable_Microwave_Linescan.metastable_microwave_linescan', 'MetastableMicrowaveLineScan'),

        (exps + 'Metastable_Microwave_Rabi_Flopping.metastable_microwave_rabi_flopping', 'MetastableMicrowaveRabiFlopping'),

        (exps + 'Rabi_Point_Tracker.rabi_point_tracker', 'RabiPointTracker'),

        (exps + 'ion_position_tracker.ion_position_tracker', 'ion_position_tracker'),

        (exps + 'Test_Pulse_Sequence.Test_Pulse_Sequence', 'TestPulseSequence'),

        (exps + 'High_Fidelity_Measurement.high_fidelity_measurement', 'high_fidelity_measurement'),

        (exps + 'Metastable_Microwave_Ramsey_Experiment.metastable_microwave_ramsey_experiment', 'MetastableMicrowaveRamseyExperiment'),

        (exps + 'Metastable_Fidelity_Tweak_Up.metastable_fidelity_tweak_up', 'metastable_fidelity_tweak_up'),

        (exps + 'Metastable_Qubit_QND.metastable_qubit_qnd', 'MetastableQubitQND'),

        (exps + 'Metastable_Measurement_Driven_Gate.metastable_measurement_driven_gate', 'metastable_measurement_driven_gate'),

        (exps + 'Metastable_Measurement_Driven_Rabi_Flop.metastable_measurement_driven_rabi_flop',
        'metastable_measurement_driven_rabi_flop'),

        (exps + 'Manifold_Detection.manifold_detection', 'manifold_detection'),

        (exps + 'Interleaved_Linescan_935.interleaved_linescan_935', 'interleaved_linescan_935'),

        (exps + 'AOM_Flickering.aom_flickering', 'aom_flickering'),

    ]

    allowed_concurrent = {}
    allowed_concurrent['Metastable Fidelity Tweak Up'] = ['Laser Monitor']
    launch_history = 1000
