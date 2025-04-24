from icecream import ic

from app.domain.service.titanic_service import TitanicService


class TitanicController:

    service = TitanicService()

    def preprocess(self, train_fname, test_fname):
        """
        Preprocess the Titanic dataset using TitanicService
        Args:
            train_fname: Training data file name
            test_fname: Test data file name
        Returns:
            Processed data object
        """
        return self.service.preprocess(train_fname, test_fname)
    
    def learning(self):
        pass

    def evaluation(self):
        pass

    def submit(self):
        pass
    
 
    
 