import sys
import math

def _nCk(n, k):
    f = math.factorial 
    return f(n) / (f(k) * f(n - k))

def _num_valid_multiset(depth, min_alt):
    """ Returns number of valid multisets of size 'depth' 
        from the set {R_fwd, R_rev, A_fwd, A_rev}. A valid multiset has at least
        'min_alt' of (A_fwd/rev) with at least one of each.
       
        Where nb = min_alt - 2
        num_valid = SUM from n_alt to depth - 2 [ ((n_alt + 1) choose 1) * \
            ((depth - 1 - n_alt) choose 1) ]
    
        !! Assumptions
            min_alt <= depth
            depth >= 3

        Valid multiset will be of the form {A_fwd, A_rev, x_3, ... x_d}
            where {x_3, ... x_d} is any multiset with exactly min_alt - 2
            A_fwd or A_rev. The other d - (min_alt) items will be 
            any R_rev or R_fwd.
    """
    def _inside_sum(depth, num_alt):
        # (#ways to arrange num_alt B/b's) * 
        #   (# ways to arrange depth - num_alt - 1 A/a's).
        return (_nCk((num_alt + 1), 1)) * (_nCk((depth - 1 - num_alt), 1))
  
    valid_count = 0 
    for curr_alt in range(min_alt - 2, (depth - 2) + 1):
        valid_count += _inside_sum(depth, curr_alt)

    return valid_count

def _num_total_multiset(depth):
    """Returns number of possible multisets of size depth from the set,
        {R_fwd, R_rev, A_fwd, A_rev}
    """
    return _nCk((depth + 3), 3)

def mutant_power(depth, min_alt):
    """
    Returns the power of mutant test at a specific depth and min_alt base.
    Mutant test is: At least one alt base in each direction, with at least
        min_alt alternate bases.
    """
    num_valid = float(_num_valid_multiset(depth, min_alt))
    total_multiset = float(_num_total_multiset(depth))

    return num_valid/total_multiset

def get_min_depth_for_power(n_alt, min_pow):
    """
    """
    min_pow = float(min_pow)

    depths = [] 
    power = []
    
    for n_depth in range(n_alt, 40):
        depths.append(n_depth)
        power.append(mutant_power(n_depth, n_alt))    
    
    print depths
    print power

    for np_depth_pos in range(0, len(power)):
        if power[np_depth_pos] >= min_pow:
            return depths[np_depth_pos]

    raise ValueError("No depth of sufficent power found")


if __name__ == "__main__":
    min_alt, req_power = int(sys.argv[1]), float(sys.argv[2])
    print get_min_depth_for_power(min_alt, req_power) 


