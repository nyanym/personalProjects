#include <iostream>

int const MAX_BOMBS = 100;
int const maxRows = 20;
int const minRows = 4;
int const maxCols = 20;
int const minCols = 4;

class Arena
{
    public:
        Arena(int bombs, int rows, int cols);
        ~Arena();

    private:
        Bomb* m_bombs[MAX_BOMBS];
        int numBombs;
        int m_rows;
        int m_cols;
};

Arena::Arena(int bombs, int rows, int cols) {
    if (bombs > MAX_BOMBS)  { numBombs = MAX_BOMBS; }
    if (bombs < 0)          { numBombs = 0; }
    if (rows > maxRows)     { m_rows = maxRows; }
    if (rows < minRows)     { m_rows = minRows; }
    if (cols > maxCols)     { m_cols = maxCols; }
    if (cols < minRows)     { m_cols = minCols; }

    for (int i = 0; i < numBombs; i++) {
        m_bombs[i] = new Bomb;
    }
}

Arena::~Arena() {
    for (int i = 0; i < numBombs; i++)
        delete m_bombs[i];
}

class Bomb
{

};

void printGrid() {

}

int countBombs() {

}

int main()
{

}