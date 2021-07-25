class Vector2D():
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def get_heading_to_point(self, point):
        return Vector2D( point[0] - self[0], point[1] - self[1] )

    def get_heading(self, point):
        return Vector2D( point[0] - self[0], point[1] - self[1] )

    def get_distance_from_point(self, point):
        heading = self.get_heading(point)
        distance = heading.get_magnitude()
        return distance

    def get_magnitude(self):
        return ( self.x**2 + self.y**2 )**.5

    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude == 0:
            self.x = 0
            self.y = 0
            return None
        self.x /= magnitude
        self.y /= magnitude


    def __add__(self, rhs):
        return Vector2D(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2D(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y

    def int_(self):
        return Vector2D(int(self.x), int(self.y))
