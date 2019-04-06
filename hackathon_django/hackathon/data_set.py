def rank_full(df, search):  
    df['title_score'] = df['title'].map(lambda x: header_ranking(x, search))
    df['body_score'] = df['body'].map(lambda y: body_ranking(y, search))   
    df['total_score'] = df['title_score'] + df['body_score']
    
    df = df.sort_values(by=['total_score'], ascending=False, inplace= True)