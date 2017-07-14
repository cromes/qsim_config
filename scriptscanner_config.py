class config(object):

    """
    scriptscanner config object for the molecules experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'Qsim.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'scan_multipole.scan_multipole', 'scan_multipole'),
			   (exps + 'wavemeter_linescan.wavemeter_linescan', 'wavemeter_linescan'),
			   (exps + 'test_DDS_channels.DDS_test_channels', 'DDS_test_channels'),
			   (exps + 'laser_stability_monitor.laser_stability_monitor', 'lasermonitor'),
			   (exps + 'TD_Flourescence.TD_flourescence', 'TD_flourescence'),
			   (exps + 'interleaved_linescan.interleaved_linescan', 'InterleavedLinescan'),
			   (exps + 'ML_Piezo_scan.ML_Piezo_scan', 'MLpiezoscan'),
			   (exps + 'line_narrowing.Line_Narrowing', 'Line_Narrowing'),
			   (exps + 'qsim_example_experiment.qsim_example_experiment', 'experiment_example'),
			   (exps + 'Metastable_Transition.metastable_transition', 'metastable_transition'),
			   (exps + 'DDS_LineScan.DDS_LineScan', 'DDS_LineScan'),
			   (exps + 'DDS_line_narrowing.DDS_Line_Narrowing', 'DDS_Line_Narrowing'),
			   (exps + 'Delay_stage_scan.Delay_stage_scan', 'Delaystagescan'),
			   (exps + 'AOM_fitting.AOM_fitting','AOM_fitting'),
			   (exps + 'tickle.tickle_experiment', 'ticklescan'),
			   ]

    allowed_concurrent = {}
    allowed_concurrent['lasermonitor'] = ['lasermonitor', 'scan_multipole']

    launch_history = 1000
