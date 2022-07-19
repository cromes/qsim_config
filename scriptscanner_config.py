class config(object):
    """
    scriptscanner config object for the molecules experiment.
    """
    # Folder names within the experiments folder that holder experiments
    path = 'Qsim.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [
        (path + 'Interleaved_Linescan.interleaved_linescan', 'InterleavedLinescan'),

        (path + 'Line_Narrowing.line_narrowing', 'LineNarrowing'),

        (path + 'Randomized_Benchmarking.randomized_benchmarking', 'RandomizedBenchmarking'),

        # (path + 'off_resonant_shelving_measurement.off_resonant_shelving_measurement',
        # 'off_resonant_shelving_measurement'),

        (path + 'Bright_State_Detection.bright_state_detection', 'BrightStateDetection'),

        (path + 'Dark_State_Detection.dark_state_detection', 'DarkStateDetection'),

        (path + 'SF_Discrimination_Experiment.sf_discrimination_experiment', 'SFDiscriminationExperiment'),

        (path + 'Coherence_Measurement.coherence_measurement', 'CoherenceMeasurement'),

        # (path + 'FFT.PMT_FFT', 'PMT_FFT'),

        # (path + 'tickle.tickle_experiment', 'ticklescan'),

        (path + 'Laser_Frequency_Tracker.laser_frequency_tracker', 'LaserFrequencyTracker'),

        (path + 'Optical_Pumping_Rate.optical_pumping_rate', 'OpticalPumpingRate'),

        # ( path + 'Quadrupole_Optical_Pumping_Linescan.quadrupole_optical_pumping_linescan',
        # 'quadrupole_optical_pumping_linescan'),

        (path + 'Fidelity_Tweak_Up.fidelity_tweak_up', 'FidelityTweakUp'),

        (path + 'Microwave_Rabi_Flopping.microwave_rabi_flopping', 'MicrowaveRabiFlopping'),

        (path + 'Microwave_Linescan.microwave_linescan', 'MicrowaveLineScan'),

        (path + 'Microwave_Linescan.microwave_linescan_minus', 'MicrowaveLineScanMinus'),

        (path + 'Microwave_Linescan.microwave_linescan_plus', 'MicrowaveLineScanPlus'),

        (
            path + 'Metastable_Microwave_Linescan_173.metastable_microwave_linescan_173',
            'MetastableMicrowaveLineScan173'),

        (path + 'Metastable_Microwave_Linescan_173.swept_metastable_microwave_linescan_173',
         'MetastableMicrowaveLineScanSwept173'),

        (path + 'Microwave_Rabi_Flopping.microwave_rabi_flopping_clock', 'MicrowaveRabiFloppingClock'),

        (path + 'Quadrupole_Linescan.quadrupole_linescan',
         'QuadrupoleLineScan'),

        #            (path + 'Quadrupole_Rabi_Flopping.quadrupole_rabi_flopping',
        #             'QuadrupoleRabiFlopping'),

        (path + 'Microwave_Ramsey_Experiment.microwave_ramsey_experiment', 'MicrowaveRamseyExperiment'),

        (path + 'High_Fidelity_Dark_State_SPAM.high_fidelity_dark_state_spam', 'HighFidelityDarkStateSpam'),

        # (path + 'DAC_Raster.DAC_Raster', 'dacRaster'),

        (path + 'Shelving_Rate.shelving_rate', 'ShelvingRate'),

        (path + 'Deshelving_Rate.deshelving_rate', 'DeshelvingRate'),

        (path + 'Wavemeter_Linescan.wavemeter_linescan', 'WavemeterLinescan'),

        # (path + 'Metastable_Microwave_Linescan.metastable_microwave_linescan', 'MetastableMicrowaveLineScan'),

        # (path + 'Metastable_Microwave_Rabi_Flopping.metastable_microwave_rabi_flopping',
        # 'MetastableMicrowaveRabiFlopping'),

        # (path + 'Rabi_Point_Tracker.rabi_point_tracker', 'RabiPointTracker'),

        #            (path + 'ion_position_tracker.ion_position_tracker', 'ion_position_tracker'),

        (path + 'Test_Pulse_Sequence.Test_Pulse_Sequence', 'TestPulseSequence'),

        (path + 'High_Fidelity_Measurement.high_fidelity_measurement', 'HighFidelityMeasurement'),

        # (path + 'Metastable_Microwave_Ramsey_Experiment.metastable_microwave_ramsey_experiment',
        # 'MetastableMicrowaveRamseyExperiment'),

        # (path + 'Metastable_Fidelity_Tweak_Up.metastable_fidelity_tweak_up', 'metastable_fidelity_tweak_up'),

        # (path + 'Metastable_Qubit_QND.metastable_qubit_qnd', 'MetastableQubitQND'),

        # (path + 'Metastable_Measurement_Driven_Gate.metastable_measurement_driven_gate',
        # 'metastable_measurement_driven_gate'),

        # (path + 'Metastable_Measurement_Driven_Rabi_Flop.metastable_measurement_driven_rabi_flop',
        # 'metastable_measurement_driven_rabi_flop'),

        (path + 'Manifold_Detection.manifold_detection', 'ManifoldDetection'),

        (path + 'Interleaved_Linescan_935.interleaved_linescan_935', 'InterleavedLinescan935'),

        (path + 'AOM_Flickering.aom_flickering', 'AOMFlickering'),

    ]

    allowed_concurrent = {'Metastable Fidelity Tweak Up': ['Laser Monitor']}
    launch_history = 1000
