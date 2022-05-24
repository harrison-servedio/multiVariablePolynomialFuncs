//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//


public class Atom implements Comparable<Atom> {//I did not know what implements or comparable mean
    private char letter;
    private int subscript = -1;
    private int power = 1;

    public Atom() {                             //Did not know the meaning of this
    }

    public Atom(char letter, int subscript, int power) {
        this.letter = letter;
        this.subscript = subscript;
        this.power = power;
    }

    public Atom(char letter) {                  //Assumend this just mean that the user would let the defaults abouve remain when creating the class
        this.letter = letter;
    }

    public char getLetter() {
        return this.letter;
    }

    public int getSubscript() {
        return this.subscript;
    }

    public int getPower() {
        return this.power;
    }

    public void setLetter(char letter) {
        this.letter = letter;
    }

    public void setSubscript(int subscript) {
        this.subscript = subscript;
    }

    public void setPower(int power) {
        this.power = power;
    }

    public void setAtom(char letter, int subscript, int power) {
        this.letter = letter;
        this.subscript = subscript;
        this.power = power;
    }

    public Atom timesLikeAtom(Atom atom) {
        return new Atom(this.getLetter(), this.subscript, this.getPower() + atom.getPower());
    }

    /** @deprecated */
    @Deprecated
    public boolean like(Atom atom) {
        return this.getLetter() == atom.getLetter() && this.getSubscript() == atom.getSubscript();
    }

    //This is the exact same thing as the like function so I don't want to make duplicates
    public boolean isLike(Atom atom) {
        return this.getLetter() == atom.getLetter() && this.getSubscript() == atom.getSubscript();
    }

    /** @deprecated */
    
    @Deprecated
    public boolean lessThanOrEqual(Atom atom) {
        if (this.getLetter() < atom.getLetter()) {
            return true;
        } else {
            if (this.getLetter() == atom.getLetter()) {
                if (this.getSubscript() < atom.getSubscript()) {
                    return true;
                }

                if (this.getSubscript() == atom.getSubscript() && this.getPower() < atom.getPower()) {
                    return true;
                }
            }

            return this.equals(atom);
        }
    }
    //same thing as the function above
    public boolean isLessThanOrEquals(Atom atom) {
        if (this.equals(atom)) {
            return true;
        } else if (this.getLetter() < atom.getLetter()) {
            return true;
        } else {
            if (this.getLetter() == atom.getLetter()) {
                if (this.getSubscript() < atom.getSubscript()) {
                    return true;
                }

                if (this.getSubscript() == atom.getSubscript() && this.getPower() < atom.getPower()) {
                    return true;
                }
            }

            return false;
        }
    }

    /** @deprecated */
    //Why doesn't this consider the power? Possible problem
    @Deprecated
    public boolean lessThan(Atom atom) {
        if (this.getLetter() < atom.getLetter()) {
            return true;
        } else {
            return this.getLetter() == atom.getLetter() && this.getSubscript() < atom.getSubscript();
        }
    }

    public boolean isLessThan(Atom atom) {
        if (this.getLetter() < atom.getLetter()) {
            return true;
        } else {
            return this.getLetter() == atom.getLetter() && this.getSubscript() < atom.getSubscript();
        }
    }

    //Same thing as equal too
    /** @deprecated */
    @Deprecated
    public boolean identicalTo(Atom atom) {
        return this.getLetter() == atom.getLetter() && this.getSubscript() == atom.getSubscript() && this.getPower() == atom.getPower();
    }

    /** @deprecated */
    @Deprecated
    public void print() {
        if (this.subscript == -1) {
            if (this.power == 1) {
                System.out.print(this.letter);
            } else if (this.power != 0) {
                System.out.print(this.letter + "^" + this.power);
            }
        } else if (this.power == 1) {
            System.out.print(this.letter + "_" + this.subscript);
        } else if (this.power != 0) {
            System.out.print(this.letter + "_" + this.subscript + "^" + this.power);
        }

    }
    //Done
    public boolean equals(Atom atom) {
        return this.getLetter() == atom.getLetter() && this.getSubscript() == atom.getSubscript() && this.getPower() == atom.getPower();
    }

    public String toString() {
        String string = "";
        if (this.subscript == -1) {
            if (this.power == 1) {
                string = String.valueOf(this.letter);
            } else if (this.power != 0) {
                string = this.letter + "^" + this.power;
            }
        } else if (this.power == 1) {
            string = this.letter + "_" + this.subscript;
        } else if (this.power != 0) {
            string = this.letter + "_" + this.subscript + "^" + this.power;
        }

        return string;
    }

    public int compareTo(Atom a) {
        if (this.equals(a)) {
            return 0;
        } else {
            return this.isLessThan(a) ? -1 : 1;
        }
    }
}
