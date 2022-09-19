using System.Numerics;
using ContinuationPassingStyle;

var quadraticEquationSolver = new QuadraticEquationSolver();
Tuple<Complex, Complex> solution;
var flag = quadraticEquationSolver.Start(1, 10, 16, out solution);

Console.WriteLine(flag == WorkflowResult.Success ? "Success :D {0}" : "Failure :(", solution);