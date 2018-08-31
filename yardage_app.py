print('knitting project yarn estimation')
print('')

# input yards per 100 stitches
yps = input('What is your yards per 100 stitches? ')

# input collar stitches
collar_s = input('How many stitches are in your collar? ')

# input collar rows
collar_r = input('How many rows in your collar? ')

# input ending yolk stitches
yolk_s = input('How many stitches are at the end of your yolk? ')

# input yolk rows
yolk_r = input('How many rows are in your yolk? ')

# input starting sleeve stitches
sleeve_st = input('How many stitches are at the beginning of your sleeve? ')

# input ending sleeve stitches
sleeve_ed = input('How many stitches are at the end of your sleeve? ')

# input sleeve rows
sleeve_r = input('How many rows are in your sleeve? ')

# input starting body stitches
body_st = input('How many stitches are at the beginning of your body? ')

# input ending body stitches
body_ed = input('How many stitches are at the end of your body? ')

# input body rows
body_r = input('How many rows are in your body? ')

collar_stitches = float(collar_s) * float(collar_r)
yolk_stitches = ((float(collar_s) + float(yolk_s))/2) * float(yolk_r)
sleeve_stitches = ((float(sleeve_st) + float(sleeve_ed))/2) * float(sleeve_r)
body_stitches = ((float(body_st) + float(body_ed))/2) * float(body_r)
total_stitches = float(collar_stitches) + float(yolk_stitches) + (float(sleeve_stitches)*2) + float(body_stitches)
yardage = total_stitches / float(yps)

print ('Your sweater will take aprox {0} yards'.format(yardage))
