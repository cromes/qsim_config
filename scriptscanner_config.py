class config(object):

        """
        scriptscanner config object for the molecules experiment.
        """
        # Folder names within the experiments folder that holder experiments
        exps = 'Qsim.scripts.experiments.'

        # list in the format (import_path, class_name)
        scripts = [
                   (exps + 'interleaved_linescan.interleaved_linescan',
                    'InterleavedLinescan'),

                   (exps + 'zeeman_fidelity.zeeman_fidelity',
                    'zeeman_fidelity'),

                
                   #(exps + 'ML_Piezo_scan.ML_Piezo_scan', 'MLpiezoscan'),

                   (exps + 'line_narrowing.Line_Narrowing', 'Line_Narrowing'),

                   #(exps + 'Delay_stage_scan.Delay_stage_scan',
                   # 'Delaystagescan'),

                   (exps + 'Bright_State_Detection.bright_state_detection', 'BrightStateDetection'),

                   (exps + 'Dark_State_Detection.dark_state_detection', 'DarkStateDetection'),

                   #(exps + 'FFT.PMT_FFT', 'PMT_FFT'),

                   #(exps + 'tickle.tickle_experiment', 'ticklescan'),

                   (exps + 'laser_stability_monitor.laser_stability_monitor',
                    'lasermonitor'),

                   (exps + 'fidelity_tweak_up.fidelity_tweak_up',
                    'fidelity_tweak_up'),

                   (exps + 'Microwave_Rabi_Flopping.microwave_rabi_flopping',
                    'MicrowaveRabiFlopping'),

                   (exps + 'Microwave_Linescan.microwave_linescan',
                    'MicrowaveLineScan'),

                   (exps + 'Quadrupole_Linescan.quadrupole_linescan',
                    'QuadrupoleLineScan'),

                   #(exps + 'Quadrupole_Rabi_Flopping.quadrupole_rabi_flopping',
                   # 'QuadrupoleRabiFlopping'),

                   #  (exps + 'pulse_runner.pulse_runner', 'PulseRunner'),

                   (exps + 'Microwave_Ramsey_Experiment.microwave_ramsey_experiment',
                    'MicrowaveRamseyExperiment'),

                   #(exps + 'AOM_fitting.AOM_fitting_experiment', 'AOM_fitting'),

                   #(exps + 'DAC_Raster.DAC_Raster', 'dacRaster'),

                   #(exps + 'ML_decoherence.ML_decoherence', 'ML_decoherence'),

                   (exps + 'shelving_411.shelving_411', 'ShelvingRate'),

                   (exps + 'deshelving_760.deshelving_760', 'DeshelvingRate'),

                   (exps + 'wavemeter_linescan.wavemeter_linescan', 'wavemeter_linescan'),

                   (exps + 'shelving_fidelity.shelving_fidelity', 'shelving_fidelity'),

                   #(exps + 'Raman_411_Scan.raman411scan', 'Raman411LineScan'),

                   (exps + 'Metastable_Microwave_Linescan.metastable_microwave_linescan',
                           'MetastableMicrowaveLineScan'),

                   (exps + 'Metastable_Microwave_Rabi_Flopping.metastable_microwave_rabi_flopping','MetastableMicrowaveRabiFlopping'),

                   #(exps + 'ion_position_tracker.ion_position_tracker', 'ion_position_tracker'),

                   #(exps + 'MM_sideband_reduction.MM_sideband_reduction', 'MM_reduction'),

                   #(exps + 'Lifetime_Measurement.Lifetime_Measurement', 'Lifetime_Measurement'),

                   #(exps + 'manifold_measurement.manifold_measurement', 'manifold_measurement'),

                   #(exps + 'TimeHarp_Interleaved.timeharp_interleaved', 'TimeHarp_Interleaved'),

                   #(exps + 'Test_Pulse_Sequence.Test_Pulse_Sequence', 'TestPulseSequence'),

                   #(exps + 'bf_fluorescence.bf_fluorescence', 'bf_fluorescence'),

                   #(exps + 'TD_Flourescence.TD_flourescence', 'TD_flourescence'),

                   #(exps + 'ML_fidelity_tweak_up.ML_fidelity_tweak_up', 'ML_fidelity_tweak_up'),

                   #(exps + 'Pulsed_delay_stage_scan.Pulsed_delay_stage_scan', 'Pulsed_delay_stage_scan'),

                   #(exps + 'hyperfine_ramsey_scan.hyperfine_ramsey_scan', 'hyperfine_ramsey_scan'),

        ]

        allowed_concurrent = {}
        allowed_concurrent['lasermonitor'] = ['lasermonitor', 'scan_multipole']
        allowed_concurrent['ML Piezo Scan'] = ['PMT_FFT', 'Tickle Scan']
        allowed_concurrent['Lifetime Measurement'] = ['Fidelity Tweak Up', 'Tickle Scan', 'Interleaved Line Scan']
        allowed_concurrent['Fidelity Tweak Up'] = ['ML Piezo Scan', 'Ramsey Delay Stage Scan', 'Interleaved Line Scan', 'Microwave Ramsey Experiment']
        launch_history = 1000
