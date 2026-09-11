import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


d1=pd.read_csv("World.csv")
print(d1)

print(d1.head())
print(d1.tail())
print(d1.columns)
print(d1.shape)
print(d1.dtypes)
d1.info()

print(d1.isna().sum())
print(d1.duplicated().sum())
# Display count of values for each column
print(d1.nunique())
print(d1["Continent"].unique())
print(d1["Country/Region"].nunique())
print(d1["Country/Region"].duplicated().sum())

# rename the columns for better reading
d1=d1.rename(columns={"Country/Region":"Country"})
d1=d1.rename(columns={"TotalCases":"Total_Cases"})
d1=d1.rename(columns={"TotalDeaths":"Total_Deaths"})
d1=d1.rename(columns={"Serious,Critical":"Critical"})
d1=d1.rename(columns={"Tot Cases/1M pop":"Cases_Per_1M"})

print(d1.columns)

print(d1.isna().sum())

# remove col permanantly

d1=d1.drop(columns=[
    "NewCases",
    "NewDeaths",
    "NewRecovered"
]
           
)
print(d1.shape)
print(d1.columns)
print(d1.isna().sum())

# finding rows with missing values
print(d1.loc[d1["Population"].isna()].to_string())
print(d1.loc[d1["Continent"].isna()].to_string())
print(d1.loc[d1["Cases_Per_1M"].isna()].to_string())
print(d1.loc[d1["TotalRecovered"].isna()].to_string())
print(d1.loc[d1["ActiveCases"].isna()].to_string())
print(d1.loc[d1["Total_Deaths"].isna()].to_string())

# remove this because isnot a counntry
d1=d1[d1["Country"]!="Diamond Princess"]
print(d1.shape)
print(d1.isna().sum())

d1["Total_Deaths"]=d1["Total_Deaths"].fillna(0)
print(d1)


print(d1.isna().sum())
print(d1.columns)


print(d1[d1["TotalRecovered"].isna()])
print(d1[d1["ActiveCases"].isna()])
print(d1[d1["Critical"].isna()])
print(d1[d1["Deaths/1M pop"].isna()])
print(d1[d1["TotalTests"].isna()])
print(d1[d1["Tests/1M pop"].isna()])
print(d1[d1["WHO Region"].isna()])

# cal death pop based on deaths and population
d1["Deaths/1M pop"]=d1["Total_Deaths"]/d1["Population"]*1000000
print(d1["Deaths/1M pop"].isna().sum())


print(d1.isna().sum())

# display missning totaltests and test1mpop missing in same rows
print(((d1["TotalTests"].isna())==(d1["Tests/1M pop"].isna())).all())

print(d1.duplicated().sum())

print(d1.dtypes)

print(d1["Country"].duplicated().sum())

# recalculate and fill active cases
d1["ActiveCases"]=d1["Total_Cases"]-d1["Total_Deaths"]-d1["TotalRecovered"]
print(d1["ActiveCases"].isna().sum())

# display country where totalrecovered is missing
print(d1.loc[d1["TotalRecovered"].isna(),["Country","Total_Cases","Total_Deaths","ActiveCases","TotalRecovered"]])
print(d1.loc[d1["TotalRecovered"].isna(),["Country","Total_Cases","Total_Deaths","ActiveCases","Population"]].to_string())

# display summary
print(d1["Critical"].describe())

# display country where critical cases are missing
print(d1.loc[d1["Critical"].isna(),["Country","Total_Cases","Critical"]])

# print country where total test is missing
print(d1.loc[d1["TotalTests"].isna(),["Country","Population","TotalTests","Tests/1M pop"]])

# display country where tests 1m is missing
print(d1.loc[d1["Tests/1M pop"].isna(),["Country","Population","TotalTests","Tests/1M pop"]])

# display country where who region is missing
print(d1.loc[d1["WHO Region"].isna(),["Country","Continent","WHO Region"]])

# show me a country that have critical cases 0
print(d1[d1["Critical"]==0][["Country","Total_Cases","Critical"]])

# count countries in WHO Region
print(d1["WHO Region"].value_counts())

who_region = {
    "French Guiana": "Americas",
    "CAR": "Africa",
    "Mayotte": "Africa",
    "Réunion": "Africa",
    "Channel Islands": "Europe",
    "Isle of Man": "Europe",
    "Guadeloupe": "Americas",
    "Martinique": "Americas",
    "Faeroe Islands": "Europe",
    "Aruba": "Americas",
    "Cayman Islands": "Americas",
    "Gibraltar": "Europe",
    "Sint Maarten": "Americas",
    "Brunei": "WesternPacific",
    "Turks and Caicos": "Americas",
    "French Polynesia": "WesternPacific",
    "St. Vincent Grenadines": "Americas",
    "Saint Martin": "Americas",
    "Macao": "WesternPacific",
    "Curaçao": "Americas",
    "New Caledonia": "WesternPacific",
    "Montserrat": "Americas",
    "Caribbean Netherlands": "Americas",
    "Falkland Islands": "Americas"
}

# loop through every country to fill values in missing region
for country,region in who_region.items():
    # update values for matching countries
    d1.loc[d1["Country"]==country,"WHO Region"]=region

# check whetheer any missing valuess left
print(d1["WHO Region"].isna().sum())

# display any countrty that have missing val left
print(d1.loc[d1["WHO Region"].isna(),["Country","Continent","WHO Region"]])

# set val 
d1.loc[d1["Country"]=="Brunei","WHO Region"]="WesternPacific"
print(d1["WHO Region"].isna().sum())

print(d1.isna().sum())

print(d1.duplicated().sum())
print(d1.dtypes)
print(d1.head())
print(d1.shape)
print(d1.columns)
d1.to_csv("Clean Covid 19 ds.csv", index=False)
print(d1)


print(d1[d1["Total_Cases"]==d1["Total_Cases"].max()])
print(d1[d1["Total_Deaths"]==d1["Total_Deaths"].max()])
print(d1[d1["TotalRecovered"]==d1["TotalRecovered"].max()])

print(d1[d1["Total_Cases"]==d1["Total_Cases"].min()])
print(d1[d1["Total_Deaths"]==d1["Total_Deaths"].min()])
print(d1[d1["TotalRecovered"]==d1["TotalRecovered"].min()])

print(d1["Total_Cases"].mean())
print(d1["Total_Deaths"].mean())
print(d1["TotalRecovered"].mean())

print(d1.groupby("Continent").agg(
    {
        "Total_Cases": ["mean"]
    }
))

print(d1.groupby("Continent").agg(
    {
        "Total_Cases": ["sum"]
    }
))
print(d1.groupby("Continent").agg(
    {
        "Total_Deaths": ["sum"]
    }
))

print(d1.groupby("Continent").agg(
    {
        "Total_Deaths": ["mean"]
    }
))
print(d1.groupby("Continent").agg(
    {
        "TotalRecovered": ["sum","mean"]
        
    }
))

print(d1.groupby("Continent").agg(
    {
        "TotalRecovered": ["sum","mean"],
        "Total_Cases":["sum","mean"],
        "Total_Deaths":["sum","mean"]
        
    }
))
print(d1.groupby("Continent").agg(
    {
        
        "Total_Cases":["sum"]
       
        
    }
))
print(d1.groupby("Continent").agg(
    {
        
        "Total_Cases":["max"]
       
        
    }
))
res=d1.groupby("Continent")["Total_Cases"].sum()
print(res.max())


print(d1.isna().sum())

print(d1.sort_values("Total_Cases",ascending=False).head(10))

print(d1.sort_values("Total_Deaths",ascending=False).head(10))

print(d1.sort_values("TotalRecovered",ascending=False).head(10))

print(d1[d1["Total_Cases"]>1000000])

print(d1[d1["Total_Deaths"]>100000])

print(d1[d1["TotalRecovered"]>500000])

print(d1[d1["Continent"]=="Asia"])

print(d1[d1["Continent"]=="Asia"].sort_values("Total_Cases",ascending=False))

print(d1[d1["Continent"]=="Asia"].sort_values("Total_Cases",ascending=False).head(5))

print(d1[d1["Continent"]=="Asia"].sort_values("Total_Deaths",ascending=False).head(5))

print(d1[d1["Continent"]=="Asia"].sort_values("TotalRecovered",ascending=False).head(5))

print(d1.sort_values("Cases_Per_1M",ascending=False).head(5))

print(d1.sort_values("Deaths/1M pop",ascending=False).head(5))


sns.histplot(data=d1,x="Total_Cases")
plt.show()

sns.barplot(data=d1,x="Continent",y="Total_Cases")
plt.show()

sns.barplot(data=d1,x="Continent",y="Total_Deaths")
plt.show()

sns.barplot(data=d1,x="Continent",y="TotalRecovered")
plt.show()

sns.histplot(data=d1,x="Total_Deaths")
plt.show()

sns.histplot(data=d1,x="TotalRecovered")
plt.show()

sns.scatterplot(data=d1,x="Total_Cases",y="Total_Deaths",hue="Continent")
plt.show()

sns.scatterplot(data=d1,x="Population",y="Total_Cases",hue="Continent")
plt.show()

co=d1.corr(numeric_only=True)
sns.heatmap(co,annot=True)

sns.countplot(data=d1,x="Continent")
plt.show()

sns.barplot(data=d1,x="Continent",y="Cases_Per_1M")
plt.show()

sns.barplot(data=d1,x="Continent",y="Deaths/1M pop")
plt.show()

sns.pairplot(d1[["Total_Cases","Total_Deaths","TotalRecovered","Population"]])
plt.show()