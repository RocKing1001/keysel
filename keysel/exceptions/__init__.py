class Error(Exception):
    """Base class for other exceptions"""
    pass


class CorrectNotInChoices(Error):
    """RAISED WHEN CORRECT CHOICE IS NOT IN CHOICES"""
    pass