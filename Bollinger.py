#initialize – Schedule Function
def initialize(context):
     context.jj = sid(4151)
     schedule_function(check_bands,date_rules.every_day())

#Check Bands
def check_bands(context, data):
    cur_price = data.current(context.jj,'price')
    prices = data.history(context.jj,'price',20,'1d')
    avg = prices.mean()
    std = prices.std()
    lower_band = avg - 2*std
    upper_band = avg + 2*std

    if cur_price <= lower_band:
         order_target_percent(context.jj,1)
         print('Buying')
    elif cur_price > upper_band:
         order_target_percent(context.jj,-1)
         print('Shorting')

    else:
         pass

    record(upper=upper_band,
           lower=lower_band,
           mavg_20 = avg,
           price = cur_price)
