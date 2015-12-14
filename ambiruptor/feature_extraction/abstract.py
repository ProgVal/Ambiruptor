class FeatureExtraction :
    """Abstract class for feature extraction"""
    
    def __init__(self) :
        """ Initialize the feature extractor. """
        pass
    
    def build(self, word) :
        """
        Build the feature extractor with the ambiguous word
        @param(word) : string
        """
        print("Feature extraction : " + word)
    
    def load(self, filename) :
        """Load a feature extractor from a binary file"""
        pass
    
    def export(self, filename) :
        """Store the feature extractor into a binary file"""
        pass
    
    def extract(self, window, pos) :
        """
        Extract a features vector.
        @param(window) : string
        @param(pos) : integer (position of the word in the sentence)
        @return : vector of features
        """
        pass
