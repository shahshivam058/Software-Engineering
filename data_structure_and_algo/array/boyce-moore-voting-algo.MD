The Boyer-Moore Voting Algorithm

The Boyer-Moore Voting Algorithm is a classic and elegant algorithm designed to find a majority element in a sequence of elements.

What is a Majority Element?
A majority element in a sequence is an element that appears more than n/2 times, where n is the length of the sequence. For example, in the array [2, 2, 1, 1, 1, 2, 2], the number 2 is the majority element because it appears 4 times in a sequence of length 7, and 47/2.

The algorithm works with a single pass through the input sequence and uses only a constant amount of extra space (O(1)). This makes it incredibly efficient.

The Core Concept: The "Counter-Strike" Analogy
Imagine a battle between a single candidate (the current "majority" contender) and all the other elements.

Candidate: A single element that we've designated as the current potential majority element.

Counter: A numerical counter that tracks the "votes" for our candidate.

The algorithm proceeds as follows:

We pick the first element as our initial candidate and set its counter to 1.

We then iterate through the rest of the sequence, one element at a time.

If the next element is the same as our candidate, our candidate gets another "vote" and we increment the counter.

If the next element is different from our candidate, that element "fights" our candidate. They cancel each other out, and we decrement the counter.

If the counter drops to zero, it means our current candidate has been defeated. It has been matched one-for-one by an equal number of non-candidate elements. At this point, we must choose a new candidate. The next element we encounter will become our new candidate, and we'll reset the counter to 1.

The crucial insight is this: If a majority element exists, it will be the last one standing when the algorithm finishes. This is because no matter how many times it gets "matched" and its counter decremented, it will eventually appear more than half the time, giving it a net positive score in the end. The final non-zero counter will belong to the true majority element.




Why Does This Work? The Proof

The elegance of the Boyer-Moore algorithm lies in its ability to discard non-majority elements without affecting the result. Let's prove why this is correct.

Claim: If an element M is a majority element, the Boyer-Moore algorithm will always return M as the final candidate.

Proof by Contradiction:

Assume M is the majority element, but the algorithm returns a different element C as the final candidate.

Let the total number of elements be n. By definition, the count of the majority element M is count(M)n/2. This means the count of all other elements combined is $count(other) \< n/2$.

The Boyer-Moore algorithm essentially pairs up different elements and removes them.

Every time we decrement the counter for our current candidate, it's because we've found an element that is not our candidate. This is like a pairing: (candidate, non-candidate).

Every time we increment the counter, we are matching a (candidate, candidate).

When the counter reaches zero, we are essentially saying that the current candidate has been paired up with an equal number of non-candidates. The number of times the counter has been decremented is equal to the number of times it has been incremented.

Consider the true majority element M. Let's analyze the counter's behavior when M is the candidate and when it's not.

Case 1: M is the current candidate. The counter will increase when we see another M and decrease when we see a non-M. Since count(M) > count(other), the number of times the counter is incremented when M is the candidate will be greater than the number of times it is decremented.

Case 2: M is not the current candidate. The counter will decrease every time we see an M. M is "fighting" against the current candidate.

Let's think about the total number of times the counter is decremented due to encountering M. This can't be more than count(M). Since count(M) > count(other), even if every single non-M element gets paired up with an M (if M is not the candidate), the Ms would still have a net "vote" advantage.

The crucial point is that every time the counter resets to zero and a new candidate is chosen, a block of elements has been processed and discarded. In each such block, the number of non-candidate elements is equal to the number of candidate elements.
If M is the majority element, its frequency is greater than the sum of all other elements' frequencies. No matter how these elements are grouped, it's impossible for M to be fully eliminated through these pairings. At the end, there must be some M elements left over. The last candidate chosen by the algorithm must have been one of these remaining Ms.




The Core Concept
The generalized algorithm for n/3 works on the same principle of vote cancellation. However, instead of a single candidate, it maintains two (candidate, count) pairs. The logic is as follows:

If the current element matches one of the candidates, increment that candidate's count.

If the current element doesn't match a candidate and there is an empty slot (a counter at zero), assign the current element to that slot and set its counter to 1.

If the current element doesn't match a candidate and both slots are full, decrement both candidates' counters. This step effectively cancels out one vote for each of the two current candidates with the single vote from the new, different element.

when we want to do n // k then total number of candidate and count we have to work is k - 1 


The General Rule

The general rule for the Boyer-Moore Voting Algorithm is that to find elements that appear more than n/k times, you need to track up to k−1 candidates.

This is based on the logic that a sequence of length n can have at most k−1 elements that each appear more than n/k times.

Example:

For n/2, k=2, so you need 2−1=1 candidate.

For n/3, k=3, so you need 3−1=2 candidates.

For n/5, k=5, so you need 5−1=4 candidates.

If you had five elements that each appeared more than n/5 times, their combined frequency would be greater than 5×(n/5)=n, which is impossible. Therefore, a maximum of k−1 such elements can exist.







