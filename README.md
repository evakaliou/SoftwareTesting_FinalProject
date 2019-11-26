# Includes: auto-constr-input-gen
A program that generates numerical inputs to programs, with support for basic range constraints.


INPUT
An amount of desired inputs, K.
A vector of vectors. Each vector corresponds to an input or set of same-type input values to be generated.

The format of a vector is:
[name_of_parameter, type_of parameter, lower_bound, upper_bound, amount]

Parameters that accept null values:
lower_bound, upper_bound

The constraints for each non-null value are:
name_of_parameter: a non-empty string. must not be a number. must not contain + - * / 
type_of_parameter: int or float
lower_bound: either ( or [, followed by a numerical expression with numbers and/or previous parameters
upper_bound: a numerical expression with numbers and/or previous parameters, followed by either ) or ]
amount: an integer greater than 0


OUTPUT
A file containing max(K,max_possible_amount_of_inputs_satisfying constraints) inputs.
