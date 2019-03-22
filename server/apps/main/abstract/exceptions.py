class FlakesErrorException(Exception):
    """Backend Flakes-app Error Exception"""
    status_code = -1  # Not OK

    def __init__(self, status_code, error_message):
        """

        :param status_code:
        :param error_message: Error Message for Client or WebHandler as a string
        """
        super(FlakesErrorException, self).__init__()
        self.status_code = status_code
        self.error_message = error_message
