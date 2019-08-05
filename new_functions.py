import pandas as pd
import math
import numbers

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', -1)


# read in the data
df = pd.read_csv('Metro_Interstate_Traffic_Volume.csv.gz', compression='gzip')
# df = pd.read_csv('train.csv') #, index_col="PassengerId")


#NOTE this is sampling with replacement
# make 50% of the data as 'historical'
hist_df = df.sample(frac=.5)

# make 50% of the data as 'new'
new_df = df.sample(frac=.5)


def get_df():
    return df


def get_hist_df():
    return hist_df


def get_new_df():
    return new_df


def unique_values(f):
    dict = {}
    # print(f.head())
    # print(f.shape)
    for label, content in f.iteritems():
        dict[label] = {}
        dict[label]['NaN'] = 0
        for i in f.index:
            # if not isinstance(content[i], str): # Realistically will have to use try/catch/except
            if isinstance(content[i], numbers.Number) and math.isnan(content[i]):
                dict[label]['NaN'] += 1
            elif content[i] not in dict[label]:
                dict[label][content[i]] = 1
            else:
                dict[label][content[i]] += 1
    return dict


def unique_types(f):
    print("\n\n\t\tTYPES\n\n")

    dict = {}
    for label, content in f.iteritems():
        # print('label:', label)
        dict[label] = {}
        dict[label]['NaN'] = 0
        for i in f.index:
            # if not isinstance(content[i], str): # Realistically will have to use try/catch/except
            if isinstance(content[i], numbers.Number) and math.isnan(content[i]):
                dict[label]['NaN'] += 1
            elif str(type(content[i])) not in dict[label]:
                dict[label][str(type(content[i]))] = 1
            else:
                dict[label][str(type(content[i]))] += 1

    return dict


def print_dict(f, dict):
    for label, content in f.iteritems():
        print("\nLabel:" + label)
        print(dict[label])


def shape_check(hist, new):
    print("hist dimensions:", str(hist.shape))
    print("new dimensions:", str(new.shape))
    if(hist.shape[0] == new.shape[0]) and (hist.shape[1] == new.shape[1]):
        return True
    else:
        return False


def NaN_check (hist,new, label, thresh):
    hist_dict = unique_values(hist)
    new_dict = unique_values(new)
    new_dict_NaN = new_dict[label]['NaN']
    hist_dict_NaN = hist_dict[label]['NaN']

    print("No. of new NaN in", label, ":", new_dict[label]['NaN'], str((new_dict[label]['NaN'])/(new.shape[0])))
    print("No. of hist NaN in", label, ":", hist_dict[label]['NaN'], str((hist_dict[label]['NaN'])/(hist.shape[0])))
    print("With threshold:", str(thresh))

    # For Raw number of NaN
    # if(new_dict[label]['NaN'] >= (1-thresh)*hist_dict[label]['NaN']) and \
    #     (new_dict[label]['NaN'] <= (1+thresh)*hist_dict[label]['NaN']):

    # For percentage of NaN from total number of records
    if(new_dict_NaN/(new.shape[0]) >= (hist_dict_NaN/(hist.shape[0]))-thresh) and \
            (new_dict_NaN/(new.shape[0]) <= thresh+(hist_dict_NaN/(hist.shape[0]))):
        return True
    else:
        return False

def NaN_check_all(hist,new,thresh):
    for label in df.columns:
        if not NaN_check(hist, new, label, thresh):
            return False
    return True


f = unique_values(df)
t = unique_types(df)
# s = set(f['date_time'])
print(t)
print("HEY\n")
# print(len(s))

date_dict = {}
count = 0
for i in f['date_time']:
    if i != 'NaN' and f['date_time'][i] > 1:
        count += 1
        print(i + " " + str(f['date_time'][i]))

# print(sorted(f['date_time'].items(), key=lambda x: x[1]))
print(len(date_dict))
print("count" + str(count))

# print_dict(df, f)

# print(f.head())

# print(type(f.at[0, 'Cabin']))
# print(math.isnan(f.at[0, 'Cabin']))
# print(f.at[0, 'Cabin'] == f.at[2, 'Cabin'])
#x
# print(f.dtypes)
# print(f.get_dtype_counts())
# print(pd.isnull(f))