//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package org.dalton.polyfun;

public class Polynomial {
    private int degree;
    private Coef[] coefs;

    public Polynomial() {
    }

    public Polynomial(Coef[] coefs) {
        this.degree = coefs.length - 1;
        this.setCoefs(coefs);
    }

    public Polynomial(double[] numericalCoefficients) {
        this.degree = numericalCoefficients.length - 1;
        this.coefs = new Coef[numericalCoefficients.length];

        for(int i = 0; i < numericalCoefficients.length; ++i) {
            this.coefs[i] = new Coef(numericalCoefficients[i]);
        }

    }

    public Polynomial(int degree) {
        this.degree = degree;
        double[] coefs = new double[degree + 1];
        coefs[degree] = 1.0D;
        this.setCoefs(coefs);
    }

    public Polynomial(double constant) {
        this.coefs = new Coef[1];
        this.coefs[0] = new Coef(constant);
        this.degree = 0;
    }

    public Polynomial(double numericalCoefficient, int degree) {
        this.coefs = new Coef[degree + 1];
        this.coefs[degree] = new Coef(numericalCoefficient);

        for(int i = 0; i < degree; ++i) {
            this.coefs[i] = new Coef(0.0D);
        }

        this.degree = degree;
    }

    public Polynomial(Atom atom) {
        this.coefs = new Coef[1];
        this.coefs[0] = new Coef(atom);
        this.degree = 0;
    }

    public Polynomial(Atom atom, int degree) {
        this.coefs = new Coef[degree + 1];
        this.coefs[degree] = new Coef(atom);

        for(int i = 0; i < degree; ++i) {
            this.coefs[i] = new Coef(0.0D);
        }

        this.degree = degree;
    }

    public Polynomial(Term term) {
        this.coefs = new Coef[1];
        this.coefs[0] = new Coef(term);
        this.degree = 0;
    }

    public Polynomial(Term term, int degree) {
        this.coefs = new Coef[degree + 1];
        this.coefs[degree] = new Coef(term);

        for(int i = 0; i < degree; ++i) {
            this.coefs[i] = new Coef(0.0D);
        }

        this.degree = degree;
    }

    public Polynomial(Coef coef) {
        this.coefs = new Coef[1];
        this.coefs[0] = coef;
        this.degree = 0;
    }

    public Polynomial(Coef coef, int degree) {
        this.coefs = new Coef[degree + 1];
        this.coefs[degree] = coef;

        for(int i = 0; i < degree; ++i) {
            this.coefs[i] = new Coef(0.0D);
        }

        this.degree = degree;
    }

    public Polynomial(char letter, int degree) {
        this.coefs = new Coef[degree + 1];
        Atom[] atoms = new Atom[degree + 1];
        Term[] terms = new Term[degree + 1];

        for(int i = 0; i < atoms.length; ++i) {
            atoms[i] = new Atom(letter, i, 1);
            terms[i] = new Term(atoms[i]);
            this.coefs[i] = new Coef(terms[i]);
        }

        this.degree = degree;
    }

    public int getDegree() {
        return this.degree;
    }

    /** @deprecated */
    @Deprecated
    public Coef getCoefficient(int index) {
        return this.coefs[index];
    }

    public Coef getCoefAt(int index) {
        return this.coefs[index];
    }

    /** @deprecated */
    @Deprecated
    public double getConstantCoefAt(int degree) {
        double constantCoefficient = 0.0D;

        try {
            constantCoefficient = this.getNumericalCoefficientAtTerm(degree);
        } catch (Exception var5) {
            System.err.println(var5.toString());
        }

        return constantCoefficient;
    }

    public double getCoefficientAtTerm(int termNumber) {
        double constantCoefficient = 0.0D;

        try {
            constantCoefficient = this.getNumericalCoefficientAtTerm(termNumber);
        } catch (Exception var5) {
            System.err.println(var5.toString());
        }

        return constantCoefficient;
    }

    public double[] getCoefficientArray() {
        double[] coefs = new double[this.getDegree() + 1];

        try {
            for(int i = 0; i < coefs.length; ++i) {
                coefs[i] = this.getCoefficientAtTerm(i);
            }
        } catch (Exception var3) {
            System.err.println(var3.toString());
        }

        return coefs;
    }

    private double getNumericalCoefficientAtTerm(int termNumber) throws AssertionError {
        if (termNumber > this.getDegree()) {
            return 0.0D;
        } else if (termNumber < 0) {
            String msg = String.format("Invalid termNumber %d for a polynomial with %d degrees.", termNumber, this.getDegree());
            throw new AssertionError(msg);
        } else {
            Coef coef = this.getCoefAt(termNumber);
            Term[] terms = coef.getTerms();
            if (terms.length == 0) {
                return 0.0D;
            } else if (terms.length == 1 && terms[0].isConstantTerm()) {
                return terms[0].getNumericalCoefficient();
            } else if (terms.length == 1) {
                return 1.0D;
            } else {
                String msg = String.format("The coefficient %s is not a constant and cannot be returned as a double.", coef.toString());
                throw new AssertionError(msg);
            }
        }
    }

    /** @deprecated */
    @Deprecated
    public Coef[] getCoefficients() {
        return this.coefs;
    }

    public Coef[] getCoefs() {
        return this.coefs;
    }

    public void setDegree(int degree) {
        this.degree = degree;
        this.coefs = new Coef[degree + 1];
    }

    /** @deprecated */
    @Deprecated
    public void setCoefficients(Coef[] coefs) {
        this.degree = coefs.length - 1;
        this.coefs = new Coef[this.degree + 1];
        System.arraycopy(coefs, 0, this.coefs, 0, this.degree + 1);
    }

    /** @deprecated */
    @Deprecated
    public void setCoefficients(double[] nums) {
        this.degree = nums.length - 1;
        this.coefs = new Coef[this.degree + 1];

        for(int i = 0; i <= this.degree; ++i) {
            this.coefs[i] = new Coef(nums[i]);
        }

    }

    public void setCoefs(Coef[] coefs) {
        this.degree = coefs.length - 1;
        this.coefs = coefs;
        Coef[] var2 = coefs;
        int var3 = coefs.length;

        for(int var4 = 0; var4 < var3; ++var4) {
            Coef coef = var2[var4];
            coef.reduce();
        }

    }

    public void setCoefs(double[] coefficients) {
        this.degree = coefficients.length - 1;
        this.coefs = new Coef[this.degree + 1];

        for(int i = 0; i <= this.degree; ++i) {
            this.coefs[i] = new Coef(coefficients[i]);
        }

    }

    public Polynomial plus(Polynomial polynomial) {
        int biggerDegree = Math.max(this.getDegree(), polynomial.getDegree());
        int smallerDegree = Math.min(this.getDegree(), polynomial.getDegree());
        Coef[] coefs = new Coef[biggerDegree + 1];

        int i;
        for(i = 0; i <= smallerDegree; ++i) {
            coefs[i] = this.getCoefAt(i).plus(polynomial.getCoefAt(i));
        }

        if (this.getDegree() > polynomial.getDegree()) {
            for(i = smallerDegree + 1; i <= biggerDegree; ++i) {
                coefs[i] = this.getCoefAt(i);
            }
        } else {
            for(i = smallerDegree + 1; i <= biggerDegree; ++i) {
                coefs[i] = polynomial.getCoefAt(i);
            }
        }

        return new Polynomial(coefs);
    }

    public Polynomial minus(Polynomial polynomial) {
        return this.plus(polynomial.times(-1.0D));
    }

    public Polynomial times(double scalar) {
        Coef[] coefs = new Coef[this.getDegree() + 1];

        for(int i = 0; i < this.getDegree() + 1; ++i) {
            coefs[i] = this.getCoefAt(i).times(scalar);
        }

        return new Polynomial(coefs);
    }

    public Polynomial times(Coef coef) {
        Coef[] coefs = new Coef[this.getDegree() + 1];

        for(int i = 0; i < this.getDegree() + 1; ++i) {
            coefs[i] = this.getCoefAt(i).times(coef);
        }

        return new Polynomial(coefs);
    }

    public Polynomial times(Polynomial polynomial) {
        Coef[] coefs = new Coef[this.getDegree() + polynomial.getDegree() + 1];

        int i;
        for(i = 0; i < coefs.length; ++i) {
            coefs[i] = new Coef(0.0D);
        }

        for(i = 0; i < coefs.length; ++i) {
            for(int j = 0; j <= i; ++j) {
                if (j <= this.getDegree() && i - j <= polynomial.getDegree()) {
                    Coef product = this.getCoefAt(j).times(polynomial.getCoefAt(i - j));
                    coefs[i] = coefs[i].plus(product);
                }
            }
        }

        return new Polynomial(coefs);
    }

    public Polynomial to(int power) {
        Polynomial polynomial = new Polynomial(1.0D);
        if (power >= 1) {
            polynomial.setCoefs(this.times(this.to(power - 1)).getCoefs());
        }

        return polynomial;
    }

    public Polynomial raiseTo(int power) {
        Polynomial polynomial;
        if (power <= 0) {
            polynomial = new Polynomial(1.0D);
        } else {
            polynomial = new Polynomial(this.getCoefs());

            for(int i = 1; i < power; ++i) {
                polynomial = this.times(polynomial);
            }
        }

        return polynomial;
    }

    public Polynomial addTangent() {
        Atom atomSlope = new Atom('m');
        Polynomial mx = new Polynomial(atomSlope, 1);
        Atom atomBias = new Atom('b');
        Polynomial b = new Polynomial(atomBias);
        Polynomial tangent = mx.plus(b);
        return this.plus(tangent);
    }

    public Polynomial of(Polynomial polynomial) {
        Polynomial result = new Polynomial(0.0D);

        for(int i = 0; i <= this.getDegree(); ++i) {
            Coef currentCoef = this.getCoefAt(i);
            Polynomial raised = polynomial.raiseTo(i);
            Polynomial product = raised.times(currentCoef);
            result.setCoefs(result.plus(product).getCoefs());
        }

        return result;
    }

    /** @deprecated */
    @Deprecated
    public Coef evaluate(double value) {
        Polynomial polynomial = new Polynomial(value);
        Coef coef = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            coef.setTerms(coef.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return coef;
    }

    public Coef evaluateToCoef(double value) {
        Polynomial polynomial = new Polynomial(value);
        Coef coef = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            coef.setTerms(coef.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return coef;
    }

    /** @deprecated */
    @Deprecated
    public double evaluateToNumber(double input) {
        Polynomial polynomial = new Polynomial(input);
        Coef coef = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            coef.setTerms(coef.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return coef.getConstantAt0Term();
    }

    public double evaluateWith(double x) {
        Polynomial polynomial = new Polynomial(x);
        Coef coef = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            coef.setTerms(coef.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return coef.getConstantAt0Term();
    }

    /** @deprecated */
    @Deprecated
    public Coef evaluate(Coef coef) {
        Polynomial polynomial = new Polynomial(coef);
        Coef result = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            result.setTerms(result.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return result;
    }

    public Coef evaluateToCoef(Coef coef) {
        Polynomial polynomial = new Polynomial(coef);
        Coef result = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            result.setTerms(result.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return result;
    }

    /** @deprecated */
    public double evaluateToNumber(Coef coef) {
        Polynomial polynomial = new Polynomial(coef);
        Coef result = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            result.setTerms(result.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return result.getConstantAt0Term();
    }

    public double evaluateWith(Coef coef) {
        Polynomial polynomial = new Polynomial(coef);
        Coef result = new Coef(0.0D);

        for(int i = 0; i < this.coefs.length; ++i) {
            result.setTerms(result.plus(polynomial.to(i).times(this.coefs[i]).getCoefAt(0)).getTerms());
        }

        return result.getConstantAt0Term();
    }

    public boolean isPlottable() {
        Coef[] var1 = this.coefs;
        int var2 = var1.length;

        for(int var3 = 0; var3 < var2; ++var3) {
            Coef coef = var1[var3];
            if (!coef.isConstantCoef()) {
                return false;
            }
        }

        return true;
    }

    /** @deprecated */
    @Deprecated
    public void print() {
        for(int i = this.degree; i > 1; --i) {
            if (!this.coefs[i].isZero()) {
                System.out.print("(");
                this.coefs[i].print();
                System.out.print(")X^" + i);

                int j;
                for(j = i - 1; j > 0 && this.coefs[j].isZero(); --j) {
                }

                if (j != 0) {
                    System.out.print("+");
                }
            }
        }

        if (this.degree > 0) {
            if (!this.coefs[1].isZero()) {
                System.out.print("(");
                this.coefs[1].print();
                System.out.print(")X");
            }

            if (!this.coefs[0].isZero()) {
                System.out.print("+");
                this.coefs[0].print();
            }
        }

        if (this.degree == 0 && !this.coefs[0].isZero()) {
            this.coefs[0].print();
        }

        System.out.println();
    }

    public String toString() {
        StringBuilder string = new StringBuilder();

        for(int i = this.getDegree(); i > 1; --i) {
            if (!this.getCoefAt(i).isZero()) {
                if (this.getCoefAt(i).isConstantCoef() && this.getCoefAt(i).getTerms()[0].getNumericalCoefficient() == 1.0D) {
                    string.append("X^").append(i);
                } else {
                    string.append("(").append(this.getCoefAt(i).toString()).append(")X^").append(i);
                }

                int prev;
                for(prev = i - 1; prev > 0 && this.getCoefAt(prev).isZero(); --prev) {
                }

                if (prev != 0) {
                    string.append("+");
                }
            }
        }

        if (this.getDegree() > 0) {
            if (!this.getCoefAt(1).isZero()) {
                if (this.getCoefAt(1).isConstantCoef() && this.getCoefAt(1).getTerms()[0].getNumericalCoefficient() == 1.0D) {
                    string.append("X");
                } else {
                    string.append("(").append(this.getCoefAt(1).toString()).append(")X");
                }
            }

            if (!this.getCoefAt(0).isZero()) {
                String constant = this.getCoefAt(0).toString();
                if (!constant.startsWith("-")) {
                    string.append("+");
                }

                string.append(constant);
            }
        } else if (this.getDegree() == 0 && !this.getCoefAt(0).isZero()) {
            string.append(this.getCoefAt(0).toString());
        }

        return string.toString().replaceAll("\\+\\Z", "");
    }
}
