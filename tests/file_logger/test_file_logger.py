# TO DO
import unittest

########################

# ça marche comme ça - jvoudrai plutôt faire from tests import ROOT_DIR mais ils me disent no module named tests alors que y'a l'init dedans jpige ap
# aussi le truc de sys.path.insert, y'a pas plus propre pour recup la classe fileLogger du dossier src ? si je rajoute pas la root au path il pige pas qui est src

########################
# import os
# import sys
# sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath()))))

# from src.file_logger.file_logger import fileLogger
# from src import ROOT_DIR
########################

from tests import ROOT_DIR

import os
import sys
sys.path.insert(1, ROOT_DIR)

from src.file_logger.file_logger import fileLogger

class TestMakeFolder(unittest.TestCase):
    
    def test_mkdir(self, fileLogger:fileLogger):
        file_logger = fileLogger()
        file_logger.make_folders()
        
        path_data = os.path.join(ROOT_DIR, 'data')
        raw_data = os.path.join(path_data, 'raw')
        
        self.assertTrue(os.path.exists(path_data))
        self.assertTrue(os.path.exists(raw_data))