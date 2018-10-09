#afds2432
#2452uhjfds


SVN

1, 2, 3... N

Given: int N - latest revision number
       run_tests(int rev): boolean - True if revision is valid, False otherwise

Goal: to find a revision where a bug has been introduced 

def search_bug(N):
  #if the very first one is invalid - all revisions are invalid
  if not run_test(1):
    return 1

  min_commit_id = 1
  max_commit_id = N
  while True:
    Midpoint = (Min_commit_id + Max_commit_id)/2
    
    if run_test(Midpoint):
    #search in later entires
      Min_commit_id = Midpoint
    else:
      Max_commit_id = Midpoint
      if run_test(Midpoint - 1):
        return Midpoint
        
      #check the entry before for validity
      #if valid, return midpoint as the first faulty entry
      #else: search lower half


  #find the mid point ID of N
  #check if that ID is valid by passing it to run_tests
  # if it is valid: 
    #check the midpoing of the second half it is more recent)
    #if it is valid repeat the above moving upwards in count
    # if it is invalid, move to midpoint down
  # if it is invalid:
    #check the midpoint between the oldest entry and the halfway point
    #if it is valid repeat the above moving upwards in count

    
    # if it is invalid, move to midpoint down
  #if the revion preceeding the one found invalid is valid -- it is the first broken one
  
- write high level comments for the parts you know first
- do not optimize until it works
- use examples
- exit conditions , remember and test
- edge case
- test exit condition on basic invariants

1   10

1 2 3
T T F
T F F
F F F 