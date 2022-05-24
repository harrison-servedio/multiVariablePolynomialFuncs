//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//



import java.util.Arrays;

public class Coef {
    private Term[] terms;

    public Coef() {
    }

    public Coef(Term[] terms) {
        this.terms = new Term[terms.length];

        for(int i = 0; i < terms.length; ++i) {
            Term term = new Term(terms[i].getNumericalCoefficient(), terms[i].getAtoms());
            term.reduce();
            this.terms[i] = term;
        }

        this.reduce();
    }

    public Coef(Term term) {
        term.reduce();
        this.setTerms(new Term[]{term});
    }

    public Coef(Atom atom) {
        Term term = new Term(atom);
        Term[] terms = new Term[]{term};
        this.setTerms(terms);
    }

    public Coef(double constant) {
        Term term = new Term(constant);
        Term[] terms = new Term[]{term};
        this.setTerms(terms);
    }

    public Coef(char letter) {
        Term term = new Term(letter);
        Term[] terms = new Term[]{term};
        this.setTerms(terms);
    }

    public Term[] getTerms() {
        return this.terms;
    }

    public void setTerms(Term[] terms) {
        this.terms = new Term[terms.length];

        for(int i = 0; i < terms.length; ++i) {
            this.terms[i] = new Term(terms[i].getNumericalCoefficient(), terms[i].getAtoms());
            this.terms[i].reduce();
        }

    }

    public void setTerms(Term term) {
        term.reduce();
        this.setTerms(new Term[]{term});
    }

    public double getConstantAt0Term() throws AssertionError {
        if (this.isZero()) {
            return 0.0D;
        } else {
            Term[] terms = this.getTerms();
            if (terms.length == 1 && terms[0].isConstantTerm()) {
                return this.getTerms()[0].getNumericalCoefficient();
            } else {
                String msg = String.format("The coef %s cannot be returned as a number", this.toString());
                throw new AssertionError(msg);
            }
        }
    }

    /** @deprecated */
    @Deprecated
    public Coef snip() {
        Term[] terms = new Term[this.getTerms().length - 1];

        for(int i = 0; i < this.getTerms().length - 1; ++i) {
            terms[i] = this.getTerms()[i + 1];
        }

        return new Coef(terms);
    }

    public Term pop() {
        if (this.getTerms().length == 0) {
            return null;
        } else {
            Term poppedTerm = this.getTerms()[0];
            Term[] terms = new Term[this.getTerms().length - 1];
            System.arraycopy(this.getTerms(), 1, terms, 0, this.getTerms().length - 1);
            this.setTerms(terms);
            return poppedTerm;
        }
    }

    /** @deprecated */
    @Deprecated
    public Coef paste(Term term) {
        Term[] terms = new Term[this.getTerms().length + 1];
        terms[0] = term;

        for(int i = 1; i < this.getTerms().length + 1; ++i) {
            terms[i] = new Term(this.getTerms()[i - 1].getNumericalCoefficient(), this.getTerms()[i - 1].getAtoms());
        }

        return new Coef(terms);
    }

    public void push(Term term) {
        Term[] terms = new Term[this.getTerms().length + 1];
        terms[0] = term;

        for(int i = 1; i < this.getTerms().length + 1; ++i) {
            terms[i] = new Term(this.getTerms()[i - 1].getNumericalCoefficient(), this.getTerms()[i - 1].getAtoms());
        }

        this.setTerms(terms);
    }

    /** @deprecated */
    @Deprecated
    public Coef place(Term term) {
        Coef coef = new Coef(this.terms);
        if (!term.isZero() && (this.getTerms() == null || this.getTerms().length == 0 || term.lessThan(this.getTerms()[0]))) {
            return coef.paste(term);
        } else {
            if (term.equals(this.getTerms()[0])) {
                coef.getTerms()[0].setNumericalCoefficient(term.getNumericalCoefficient() + coef.getTerms()[0].getNumericalCoefficient());
            } else if (this.getTerms().length == 1) {
                Term[] terms = new Term[]{term};
                Coef coef1 = new Coef(terms);
                coef.setTerms(coef1.paste(this.getTerms()[0]).getTerms());
            } else {
                Term term1 = this.getTerms()[0];
                coef.setTerms(coef.snip().place(term).paste(term1).getTerms());
            }

            return coef;
        }
    }

    public void insert(Term term) {
        if (term != null && !term.isZero()) {
            if (this.getTerms() == null || this.getTerms().length == 0) {
                this.setTerms(term);
                return;
            }

            for(int i = 0; i < this.getTerms().length; ++i) {
                if (term.equals(this.getTerms()[i])) {
                    double sum = term.getNumericalCoefficient() + this.getTerms()[i].getNumericalCoefficient();
                    this.getTerms()[i].setNumericalCoefficient(sum);
                    return;
                }
            }

            this.push(term);
            Arrays.sort(this.getTerms());
        }

    }

    public Coef simplify() {
        Coef coef = new Coef(this.getTerms());
        if (this.getTerms().length > 1) {
            Term term = new Term(this.getTerms()[0].simplify().getNumericalCoefficient(), this.getTerms()[0].simplify().getAtoms());
            this.setTerms(coef.snip().simplify().place(term).getTerms());
        } else if (this.getTerms().length == 1) {
            Term[] terms = new Term[]{this.getTerms()[0].simplify()};
            this.setTerms(terms);
        }

        return this;
    }

    public void reduce() {
        Term[] termsUnordered = new Term[this.getTerms().length];
        System.arraycopy(this.getTerms(), 0, termsUnordered, 0, this.getTerms().length);
        this.setTerms(new Term[0]);

        for(int i = 0; i < termsUnordered.length; ++i) {
            termsUnordered[i].reduce();
            this.insert(termsUnordered[i]);
        }

    }

    public Coef times(Coef coef) {
        Term[] terms = new Term[this.getTerms().length * coef.getTerms().length];

        for(int i = 0; i < this.getTerms().length; ++i) {
            for(int j = 0; j < coef.getTerms().length; ++j) {
                Term product = this.getTerms()[i].times(coef.getTerms()[j]);
                int index = i * coef.getTerms().length + j;
                terms[index] = product;
            }
        }

        Coef productCoef = new Coef(terms);
        productCoef.reduce();
        return productCoef;
    }

    public Coef times(double scalar) {
        Term[] terms = new Term[this.getTerms().length];

        for(int i = 0; i < this.getTerms().length; ++i) {
            terms[i] = this.getTerms()[i].times(scalar);
        }

        return new Coef(terms);
    }

    public Coef plus(Coef coef) {
        if (this.isZero() && coef.isZero()) {
            return new Coef(0.0D);
        } else if (coef.isZero()) {
            return this;
        } else if (this.isZero()) {
            return coef;
        } else {
            Term[] terms = new Term[this.getTerms().length + coef.getTerms().length];

            for(int i = 0; i < terms.length; ++i) {
                if (i < this.getTerms().length) {
                    terms[i] = this.getTerms()[i];
                } else {
                    terms[i] = coef.getTerms()[i - this.getTerms().length];
                }
            }

            Coef sum = new Coef(terms);
            sum.reduce();
            return sum;
        }
    }

    public boolean isZero() {
        this.reduce();

        for(int i = 0; i < this.getTerms().length; ++i) {
            if (!this.getTerms()[i].isZero()) {
                return false;
            }
        }

        return true;
    }

    /** @deprecated */
    @Deprecated
    public boolean isDouble() {
        this.simplify();
        return this.terms.length == 1 && this.terms[0].isDouble();
    }

    public boolean isConstantCoef() {
        this.reduce();
        return this.terms.length == 1 && this.terms[0].isConstantTerm();
    }

    /** @deprecated */
    @Deprecated
    public void print() {
        if (this.terms[0].getNumericalCoefficient() != 0.0D) {
            this.terms[0].print();
        }

        for(int i = 1; i < this.terms.length; ++i) {
            if (this.terms[i].getNumericalCoefficient() > 0.0D) {
                System.out.print("+");
                this.terms[i].print();
            } else if (this.terms[i].getNumericalCoefficient() < 0.0D) {
                this.terms[i].print();
            }
        }

    }

    public String toString() {
        String string = "";
        if (this.terms.length > 0) {
            string = string + this.getTerms()[0].toString();
        }

        for(int i = 1; i < this.getTerms().length; ++i) {
            String term = this.getTerms()[i].toString();
            if (term.length() > 0) {
                if (string.length() > 0 & this.getTerms()[i].getNumericalCoefficient() > 0.0D) {
                    string = string + "+";
                }

                string = string + term;
            }
        }

        return string;
    }
}
