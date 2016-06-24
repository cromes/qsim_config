class config(object):

    """
    scriptscanner config object for the molecules experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'Qsim.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'tickle.tickle_experiment', 'ticklescan'),
	       (exps + 'wavemeter_linescan.wavemeter_linescan', 'wavemeter_linescan'),
               (exps + 'test_DDS_channels.DDS_test_channels', 'DDS_test_channels'),
	       (exps + 'laser_stability_monitor.laser_stability_monitor', 'lasermonitor'),
	       (exps + 'M2_pump_monitor.M2_pump_monitor', 'M2pumpmonitor'),
	       (exps + 'testexp.testexperiment', 'testexperiment'),
	       (exps + 'DAC_Raster.DAC_Raster', 'dacRaster')
               ]

    allowed_concurrent = {}
    allowed_concurrent['lasermonitor'] = ['lasermonitor']
    
    launch_history = 1000   
