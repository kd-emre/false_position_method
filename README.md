# false_position_method
## What is False Position Method?
False Position Method, also known as Regula Falsi, is a numerical method for finding the roots of a function. This method uses iterative approximation techniques.

In this code, we've utilized a simple polynomial function, like **$x^2 - x - 1$**, as an example. We've specifically chosen this basic function because it's crucial to know that such a function always has a root. If, however, the function doesn't have a root, the program will notify us accordingly. If you're uncertain whether a function has a root or not, you can refer to the **Intermediate Value Theorem** for guidance.

Basically, in this method, we examine two points and the value of the function at these points. If the multiplication of these function values is negative, we can determine that a root exists between these points. Afterwards, we generate a new point. We then consider these three points and select two of them where the multiplication of the function values is negative. This process constitutes one iteration. With more iterations, the results get closer to the actual root value.

You can also examine the root of this function between 1 and 5 without changing anything in the program. 
