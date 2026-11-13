# Desktop tests for ti84/INTEREST.py and ti84/ANNUITY.py (not for the calculator).
# Run: python3 tests/test_interest.py
import builtins, os, sys
builtins.INTEREST_TEST = True  # stops the menu from running on import
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ti84'))
from INTEREST import gf, lump_t, lump_r, apy, simple
from ANNUITY import fv, pv, ann_n, ann_r

fails = 0
def check(name, got, want, tol):
    global fails
    ok = got is not None and abs(got - want) <= tol
    if not ok:
        fails += 1
    print(('PASS ' if ok else 'FAIL ') + name + ': got ' + repr(got) + ', want ' + repr(want))

check('compound $5000 4% qtr 6y', 5000 * gf(.04, 4, 6), 6348.67, .005)
check('t $1200->$3000 7% monthly', lump_t(1200, 3000, .07, 12), 13.13, .005)
check('double at 5% continuous', lump_t(1, 2, .05, 0), 13.86, .005)
check('APY 6% monthly (%)', apy(.06, 12) * 100, 6.1678, .00005)
check('APY 6% continuous (%)', apy(.06, 0) * 100, 6.1837, .00005)
check('FV ordinary $200/mo 6% 10y', fv(200, .005, 120, 0), 32775.87, .005)
check('FV due $200/mo 6% 10y', fv(200, .005, 120, 1), 32939.75, .005)
n = ann_n(32775.87, 200, .005, 0, True)
check('n from FV ordinary', n, 120, .001)
check('t = n/m', n / 12, 10, .0001)
check('r from FV ordinary (%)', ann_r(32775.87, 200, 12, 120, 0, True) * 100, 6.0, .00005)
check('sinking fund R $50000 8y 5% qtr', 50000 / fv(1, .0125, 32, 0), 1280.40, .005)
check('PV ordinary $1500/mo 20y 4.8%', pv(1500, .004, 240, 0), 231139.95, .005)
check('PV due $1500/mo 20y 4.8%', pv(1500, .004, 240, 1), 232064.51, .005)
check('n from PV ordinary', ann_n(231139.95, 1500, .004, 0, False), 240, .001)
I, A = simple(1000, .05, 3)
check('simple I', I, 150, 1e-9)
check('simple A', A, 1150, 1e-9)
# extra edge cases
check('r from PV due (%)', ann_r(232064.51, 1500, 12, 240, 1, False) * 100, 4.8, .00005)
check('n from FV due', ann_n(32939.75, 200, .005, 1, True), 120, .001)
print('never pays off ->', ann_n(100000, 300, .005, 0, False))
check('compound r back out (%)', lump_r(5000, 6348.67, 4, 6) * 100, 4.0, .0001)
print('ALL PASS' if fails == 0 else str(fails) + ' FAILED')
sys.exit(1 if fails else 0)
