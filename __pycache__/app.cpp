#include <iostream>

using namespace std;

class Rectangle {
private:
    int length;
    int breadth;

public:
    Rectangle(int length, int breadth) : length(length), breadth(breadth) {}

    int area() {
        return length * breadth;
    }

    int perimeter() {
        return 2 * (length + breadth);
    }
};

class Cuboid : public Rectangle {
private:
    int height;

public:
    Cuboid(int length, int breadth, int height) : Rectangle(length, breadth), height(height) {}

    int volume() {
        return length * breadth * height;
    }
};

int main() {
    Rectangle r(19, 20);
    Cuboid c(19, 20, 21);

    cout << "Rectangle Area: " << r.area() << endl;
    cout << "Rectangle Perimeter: " << r.perimeter() << endl;

    cout << "Cuboid Volume: " << c.volume() << endl;

    return 0;
}
