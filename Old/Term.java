//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package org.dalton.polyfun;

import java.util.Arrays;

public class Term implements Comparable<Term> {
    private double numericalCoefficient;
    private Atom[] atoms;

    public Term() {
    }

    public Term(double constant) {
        this.numericalCoefficient = constant;
        this.atoms = new Atom[0];
    }

    public Term(Atom atom) {
        this.numericalCoefficient = 1.0D;
        this.atoms = new Atom[]{atom};
    }

    public Term(char letter) {
        this.numericalCoefficient = 1.0D;
        this.atoms = new Atom[]{new Atom(letter)};
    }

    public Term(double numericalCoefficient, Atom[] atoms) {
        this.numericalCoefficient = numericalCoefficient;
        if (atoms != null) {
            this.atoms = new Atom[atoms.length];
            System.arraycopy(atoms, 0, this.atoms, 0, atoms.length);
        }

    }

    /** @deprecated */
    @Deprecated
    public double getTermDouble() {
        return this.numericalCoefficient;
    }

    public double getNumericalCoefficient() {
        return this.numericalCoefficient;
    }

    /** @deprecated */
    @Deprecated
    public Atom[] getTermAtoms() {
        return this.atoms;
    }

    public Atom[] getAtoms() {
        return this.atoms;
    }

    /** @deprecated */
    @Deprecated
    public void setTerm(double num, Atom[] atoms) {
        this.numericalCoefficient = num;
        this.atoms = atoms;
        this.reduce();
    }

    /** @deprecated */
    @Deprecated
    public void setTermDouble(double num) {
        this.numericalCoefficient = num;
    }

    /** @deprecated */
    @Deprecated
    public void setTerm(Atom[] atoms) {
        this.atoms = atoms;
    }

    public void setNumericalCoefficient(double numericalCoefficient) {
        this.numericalCoefficient = numericalCoefficient;
    }

    public void setAtoms(Atom[] atoms) {
        this.atoms = atoms;
    }

    public Atom pop() {
        if (this.getAtoms() == null && this.getAtoms().length == 0) {
            return null;
        } else {
            Atom[] atoms = new Atom[this.getAtoms().length - 1];
            Atom removed = this.getAtoms()[0];

            for(int i = 0; i < atoms.length; ++i) {
                atoms[i] = this.getAtoms()[i + 1];
            }

            this.setAtoms(atoms);
            return removed;
        }
    }

    public Term snip() {
        Atom[] atoms = new Atom[this.getAtoms().length - 1];

        for(int i = 0; i < atoms.length; ++i) {
            atoms[i] = this.getAtoms()[i + 1];
        }

        return new Term(this.numericalCoefficient, atoms);
    }

    public Term paste(Atom atom) {
        Atom[] atoms = new Atom[this.atoms.length + 1];
        atoms[0] = atom;
        System.arraycopy(this.atoms, 0, atoms, 1, atoms.length - 1);
        return new Term(this.numericalCoefficient, atoms);
    }

    public void push(Atom atom) {
        Atom[] atoms = new Atom[this.atoms.length + 1];
        atoms[0] = atom;
        System.arraycopy(this.atoms, 0, atoms, 1, atoms.length - 1);
        this.setAtoms(atoms);
    }

    public void append(Atom atom) {
        Atom[] atoms = new Atom[this.atoms.length + 1];
        System.arraycopy(this.atoms, 0, atoms, 0, atoms.length - 1);
        atoms[atoms.length - 1] = atom;
        this.setAtoms(atoms);
    }

    public Term place(Atom atom) {
        Term term = new Term(this.numericalCoefficient, this.atoms);
        if (atom.isLessThan(this.atoms[0])) {
            return term.paste(atom);
        } else {
            Atom atom1;
            if (atom.isLike(this.atoms[0])) {
                atom1 = this.atoms[0];
                return term.snip().paste(atom1.timesLikeAtom(atom));
            } else if (this.atoms.length == 1) {
                atom1 = new Atom(atom.getLetter(), atom.getSubscript(), atom.getPower());
                Atom[] atoms1 = new Atom[]{atom1};
                Term term1 = new Term(this.numericalCoefficient, atoms1);
                return term1.paste(this.atoms[0]);
            } else {
                atom1 = new Atom();
                atom1.setAtom(this.atoms[0].getLetter(), this.atoms[0].getSubscript(), this.atoms[0].getPower());
                return term.snip().place(atom).paste(atom1);
            }
        }
    }

    public void insert(Atom atom) {
        if (this.getAtoms() != null && this.getAtoms().length != 0) {
            if (atom.isLessThan(this.atoms[0])) {
                this.push(atom);
            } else {
                Atom head;
                if (atom.isLike(this.atoms[0])) {
                    head = this.pop();
                    this.push(head.timesLikeAtom(atom));
                } else if (this.atoms.length == 1) {
                    this.append(atom);
                } else {
                    head = this.pop();
                    this.insert(atom);
                    this.push(head);
                }
            }
        } else {
            this.setAtoms(new Atom[]{atom});
        }

    }

    public Term simplify() {
        if (this.atoms != null && this.atoms.length > 1) {
            Atom atom = new Atom(this.atoms[0].getLetter(), this.atoms[0].getSubscript(), this.atoms[0].getPower());
            Term term = new Term(this.numericalCoefficient, this.atoms);
            term = term.snip().simplify().place(atom);
            this.setAtoms(term.getAtoms());
        }

        return this;
    }

    public void reduce() {
        if (this.getAtoms() != null) {
            Atom[] unorderedAtoms = this.getAtoms();
            this.atoms = new Atom[0];

            for(int i = 0; i < unorderedAtoms.length; ++i) {
                if (unorderedAtoms[i].getPower() != 0) {
                    this.insert(unorderedAtoms[i]);
                }
            }

        }
    }

    public Term times(Term term) {
        if (this.atoms != null && term.atoms != null) {
            Atom[] atoms = new Atom[this.atoms.length + term.getAtoms().length];

            for(int i = 0; i < atoms.length; ++i) {
                if (i < this.atoms.length) {
                    atoms[i] = this.atoms[i];
                } else {
                    atoms[i] = term.getAtoms()[i - this.atoms.length];
                }
            }

            Term termProduct = new Term(this.numericalCoefficient * term.getNumericalCoefficient(), atoms);
            termProduct.reduce();
            return termProduct;
        } else {
            return term;
        }
    }

    public Term times(double scalar) {
        return new Term(scalar * this.getNumericalCoefficient(), this.getAtoms());
    }

    /** @deprecated */
    @Deprecated
    public boolean like(Term term) {
        Term term1 = new Term(this.simplify().getNumericalCoefficient(), this.simplify().getAtoms());
        Term term2 = new Term(term.simplify().getNumericalCoefficient(), term.simplify().getAtoms());
        int len = 0;
        if (term1.getAtoms().length != term2.getAtoms().length) {
            return false;
        } else {
            for(int i = 0; i < term1.getAtoms().length; ++i) {
                if (term1.getAtoms()[i].like(term2.getAtoms()[i])) {
                    ++len;
                }
            }

            return len == term1.getAtoms().length;
        }
    }

    public boolean isLike(Term term) {
        this.reduce();
        term.reduce();
        if (this.getAtoms().length != term.getAtoms().length) {
            return false;
        } else {
            for(int i = 0; i < this.getAtoms().length; ++i) {
                if (!this.getAtoms()[i].isLike(term.getAtoms()[i])) {
                    return false;
                }
            }

            return true;
        }
    }

    /** @deprecated */
    @Deprecated
    public boolean lessThan(Term term) {
        int len = 0;
        term.simplify();
        this.simplify();
        Term term1 = new Term(this.getNumericalCoefficient(), this.getAtoms());
        Term term2 = new Term(term.getNumericalCoefficient(), term.getAtoms());
        if (term1.getAtoms().length <= term2.getAtoms().length && !this.equals(term)) {
            for(int i = 0; i < term1.getAtoms().length; ++i) {
                if (term1.getAtoms()[i].lessThanOrEqual(term2.getAtoms()[i])) {
                    ++len;
                }
            }

            return len == term1.getAtoms().length;
        } else {
            return false;
        }
    }

    public boolean isZero() {
        return this.numericalCoefficient == 0.0D;
    }

    /** @deprecated */
    @Deprecated
    public boolean isDouble() {
        return this.atoms.length == 0;
    }

    public boolean isConstantTerm() {
        boolean isConstantTerm = false;
        if (this.getAtoms().length == 0) {
            isConstantTerm = true;
        } else if (this.getAtoms().length == 1 && this.getAtoms()[0].toString() == "") {
            isConstantTerm = true;
        }

        return isConstantTerm;
    }

    /** @deprecated */
    @Deprecated
    public boolean identicalTo(Term term) {
        Term term1 = new Term(this.simplify().getNumericalCoefficient(), this.simplify().getAtoms());
        Term term2 = new Term(term.simplify().getNumericalCoefficient(), term.simplify().getAtoms());
        int len = 0;
        if (term1.getAtoms().length != term2.getAtoms().length) {
            return false;
        } else {
            for(int i = 0; i < term1.getAtoms().length; ++i) {
                if (term1.getAtoms()[i].equals(term2.getAtoms()[i])) {
                    ++len;
                }
            }

            return len == term1.getAtoms().length;
        }
    }

    /** @deprecated */
    @Deprecated
    public void print() {
        if (this.atoms.length == 0 && this.numericalCoefficient != 0.0D) {
            System.out.print(this.numericalCoefficient);
        } else {
            int i;
            if (this.numericalCoefficient == 1.0D) {
                for(i = 0; i < this.atoms.length; ++i) {
                    this.atoms[i].print();
                }
            } else if (this.numericalCoefficient == -1.0D) {
                System.out.print("-");

                for(i = 0; i < this.atoms.length; ++i) {
                    this.atoms[i].print();
                }
            } else {
                System.out.print(this.numericalCoefficient);

                for(i = 0; i < this.atoms.length; ++i) {
                    this.atoms[i].print();
                }
            }
        }

    }

    public boolean equals(Term term) {
        this.reduce();
        term.reduce();
        if (term == null) {
            return false;
        } else if (this.getAtoms() == null && term.getAtoms() == null) {
            return true;
        } else if (this.getAtoms() == null) {
            return false;
        } else if (term.getAtoms() == null) {
            return false;
        } else if (this.getAtoms().length == term.getAtoms().length) {
            for(int i = 0; i < this.getAtoms().length; ++i) {
                if (!this.getAtoms()[i].equals(term.getAtoms()[i])) {
                    return false;
                }
            }

            return true;
        } else {
            return false;
        }
    }

    public String toString() {
        StringBuilder string = new StringBuilder();
        if (this.numericalCoefficient == 0.0D) {
            return "";
        } else if (this.atoms != null && this.atoms.length != 0) {
            if (this.numericalCoefficient == -1.0D) {
                string.append("-");
            } else if (this.numericalCoefficient != 1.0D) {
                string.append(String.valueOf(this.numericalCoefficient));
            }

            for(int i = 0; i < this.atoms.length; ++i) {
                string.append(this.atoms[i].toString());
            }

            return string.toString();
        } else {
            return String.valueOf(this.numericalCoefficient);
        }
    }

    public int compareTo(Term t) {
        if (t.isConstantTerm() && this.isConstantTerm()) {
            if (this.getNumericalCoefficient() == t.getNumericalCoefficient()) {
                return 0;
            } else {
                return this.getNumericalCoefficient() > t.getNumericalCoefficient() ? 1 : -1;
            }
        } else if (t.isConstantTerm()) {
            return -1;
        } else if (this.isConstantTerm()) {
            return 1;
        } else {
            Term thisTerm = new Term(1.0D, this.getAtoms());
            Term thatTerm = new Term(1.0D, t.getAtoms());
            Arrays.sort(thisTerm.getAtoms());
            Arrays.sort(thatTerm.getAtoms());
            String theseAtoms = thisTerm.toString();
            String thoseAtoms = thatTerm.toString();
            if (theseAtoms.equals(t)) {
                return 0;
            } else {
                return theseAtoms.compareToIgnoreCase(thoseAtoms) < 0 ? -1 : 1;
            }
        }
    }
}

