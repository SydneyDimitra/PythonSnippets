"""Code that deals with Shotgun Projects. """
from shotgun.common import conn


class ShotgunShot(): 
    """Object to store shot information from Shotgun."""

    def __init__(self, show_name, shot_name):
        """Init.

        Args:
            show_name (basestring): The name of the show.
            shot_name (basestring): The name of the shot.
        """
        filters = [
            ['project.Project.name', 'is', show_name],
            ['code', 'is', shot_name],
        ]
        searcher = _utils.ShotgunSearch(ENTITY_TYPE, ENTITY_FIELDS)
        shot_info = searcher(filters)
        super(ShotgunShot, self).__init__(shot_info)

    @property
    def name(self):
        return self._code

    def __repr__(self):
        """Object representation."""
        return "{0}<id:{1} name:{2}>".format(
            self.__class__.__name__,
            self.id,
            self.name
        )

    def __eq__(self, other):
        """Object equality."""
        return (
            isinstance(other, self.__class__)
            and other.id == self.id
            and other.name == self.name
        )
