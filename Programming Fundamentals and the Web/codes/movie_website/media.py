import webbrowser


class Video:
    """This class contains basic properties of a video.

    Attributes:
        title (str): Title of video
        duration (number): Number of minutes
    """

    def __init__(self, title, duration=0):
        self.title = title
        self.duration = duration


class Movie(Video):
    """This class defines some info of a movie and opens youtube
    trailer in a new browser's tab.

    Attributes:
        storyline (str): Storyline of video
        poster_image_url (str): Link of box art image
        trailer_youtube_url (str): Link of youtube's video trailer
    """

    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        Video.__init__(self, movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open new tab in web browser with youtube trailer url """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """This class defines properties of a TvShow

    Attributes:
        season (number): Season of this TvShow
        number_of_episodes (number) : Number of episodes in this TvShow
        tv_station (number): Producer of this TvShow
    """

    def __init__(self, tv_show_title, season, number_of_episodes, tv_station):
        Video.__init__(tv_show_title)
        self.season = season
        self.number_of_episodes = number_of_episodes
        self.tv_station = tv_station

    def get_local_listings(self):
        pass
