import urllib.parse

class Embed:
    def __init__(self, title, **args) -> None:
        """
        Parameters:
            description (str): Description of embed (max 340 characters)
            color/colour (str): Color of embed. (hex)
            url (str): Url of embed.
        """
        description = args.get("description", "")
        color = args.get("color", "") or args.get("colour", "") or "000000"
        url = args.get("url", "")

        if isinstance(color, int):
            color = str(hex(color)[2:])

        elif isinstance(color, str):
            if color.startswith("#"):
                color = color[1:]
            elif color.startswith("0x"):
                color = color[2:]

        self.params = {
            "title": title,
            "description": description,
            "color": color,
            "url": url
        }

    def set_title(self, title) -> None:
        """
        Sets title of embed.
        """

        self.params["title"] = title

    def set_description(self, description) -> None:
        """
        Sets description of embed.
        """

        self.params["description"] = description

    def set_colour(self, colour) -> None:
        """
        Sets colour of embed.

        Parameters:
            colour (str): Colour of embed.
        """

        self.params["color"] = colour

    def set_color(self, color) -> None:
        """
        Sets color of embed.

        Parameters:
            color (str): Color of embed.
        """

        self.params["color"] = color

    def set_author(self, name, *, url="") -> None:
        """
        Sets author of embed.

        Parameters:
            name (str): Name of author.
            url (str): Url to redirect to when author is clicked.
        """

        self.params["author"] = name

        """if url:
            self.params["redirect"] = url"""

    def set_provider(self, name, *, url="") -> None:
        """
        Sets provider of embed.

        Parameters:
            name (str): Name of provider.
            url (str): Url to redirect to when provider is clicked.
        """

        self.params["provider_name"] = name

        """if url:
            self.params["provider_url"] = url"""

    def set_image(self, url) -> None:
        """
        Sets image of embed.

        Parameters:
            url (str): Url of image.
        """

        self.params["image"] = url

    def set_video(self, url) -> None:
        """
        Sets video of embed.

        Parameters:
            url (str): Url of video.
        """

        self.params["video"] = url

    def generate_url(self, *, hide_url=False) -> str:
        """
        Generates url of embed.
        """

        for key in list(self.params.keys()):
            if self.params[key] == "" or self.params[key] is None:
                del self.params[key]

        url = "https://discord-embed-api.onrender.com/generateEmbed?" + urllib.parse.urlencode(self.params)

        if hide_url:
            return "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||" + " " + url
        else:
            return url

    set_color = set_colour
