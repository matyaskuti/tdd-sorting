# Sorting with Test Driven Development and the Transformation Priority Premise

The contents of this repository are to demonstrate a Python implementation of
some sorting algorithms using TDD and the difference between favouring low
or high priority transformations, as introduced by
[Uncle Bob](https://en.wikipedia.org/wiki/Robert_C._Martin) in several mediums:
 * [Transformation Priority and Sorting](http://blog.cleancoder.com/uncle-bob/2013/05/27/TransformationPriorityAndSorting.html)
 * [Transformation Priority Premise](http://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)
 * [Transformation Priority Premise, Ep. 1](https://cleancoders.com/episode/clean-code-episode-24-p1/show)
 * [Transformation Priority Premise, Ep. 2](https://cleancoders.com/episode/clean-code-episode-24-p2/show)

According to the Transformation Priority Premise refactorings have
counterparts, _transformations_. These actually change the behaviour of our
code. However if one uses these transformations according to their priority
in the test driven development process, by striving for adding minimal
complexity in each step, one would end up with simpler and more effective code.

## Explanation

If you browse through the commit history of this repository, you'll see a step
by step TDD implementation of two list sorting algorithms:
bubble and quicksort respectively. The extended commit messages explain the
thought process and issues encountered in each step.

Each commit message from the TDD process looks like the following:
`[<TDD PHASE>] <message> (<transformation>)`.

Where the `TDD PHASE` could be:
 * `RED` - meaning a new failing testcase, or part of the solution towards
 making the testcase pass, while the tests are still failing
 * `GREEN` - making a new testcase pass
 * `REFACTOR` - change code while keeping the testcases passing, no change in
 behaviour

 And the transformation refers to one of the following as introduced by
 Uncle Bob:
 1. Null
 2. Null to constant
 3. Constant to variable
 4. Add computation
 5. Split flow
 6. Variable to array
 7. Array to container
 8. If to while
 9. Recurse
 10. Iterate
 11. Assign
 12. Add case

To see the commits and their respective changes in order of creation, run
after checking out the repository:

    git log -p -w -M -M --reverse

## Running the tests
To run the tests at any given step (commit), just do the following:

    $ python test_sort.py

## Disclaimer

The end result of the second algorithm (quicksort) is flawed. If you were to
run it with a large (1000 or more elements) list that is ordered, you'd get a
`RuntimeError` because of the exceeded maximum recursion depth.
This is due to all recursion happening on "one stack" - the divide and conquer
tree is degenerate and looks more like a linked list.

Example:

    >>> from sort import quick_sort
    >>> quick_sort(range(1000))
    ...
    >>> RuntimeError: maximum recursion depth exceeded

Call stack of an ordered list (6 deep):

    quick_sort([1, 2, 3, 4, 5])
    ├── quick_sort([])
    └── quick_sort([2, 3, 4, 5])
        ├── quick_sort([])
        └── quick_sort([3, 4, 5])
            ├── quick_sort([])
            └── quick_sort([4, 5])
                ├── quick_sort([])
                └── quick_sort([5])
                    ├── quick_sort([])
                    └── quick_sort([])

Now compare it to the call stack of an unordered list of the same length
(4 deep):

    quick_sort([2, 4, 5, 3, 1])
    ├── quick_sort([1])
    │   ├── quick_sort([])
    │   └── quick_sort([])
    └── quick_sort([4, 5, 3])
        ├── quick_sort([3])
        │   ├── quick_sort([])
        │   └── quick_sort([])
        └── quick_sort([5])
            ├── quick_sort([])
            └── quick_sort([])

A possible solution would be not to base partitioning of the list to lower and
higher elements on the very first number (index 0) in the list. But rather
choose the _actual_ middle element. This way the list length would dramatically
increase before we hit a recursion limit.
