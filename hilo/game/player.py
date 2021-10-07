class Player:
    """
    This is the player class which handles
    the user input for the game
    """

    def call(self):
        """
        Askes the player whether or not they
        want to call high or low
        """
        valid_response = False
        #keeps asking the user for input until they give
        # a valid response.
        while valid_response is False:
            response = input("Do you want to call High or Low? (h/l) ")
            #Checks to see if user inputed a valid response.
            if response.lower == "high" or response.lower == "low" or response.lower == "h" or response.lower == "l":
                valid_response = True
        return response