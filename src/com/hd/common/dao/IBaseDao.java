package com.hd.common.dao;

import java.util.List;
import java.util.Map;

public interface IBaseDao<M extends java.io.Serializable, PK extends java.io.Serializable> {
    
    public PK save(M model);

    public void saveOrUpdate(M model);
    
    public void update(M model);
    
    public void merge(M model);

    public void delete(PK id);

    public void deleteObject(M model);

    public M get(PK id);
    
    public int countAll();

    public List<M> listAll();

    boolean exists(PK id);
    
    public List exesqlrelist(String sql,List<Object> paramlist);

    public List exehqlrelist(String hql,List<Object> paramlist);
    
    public M exesqlreM(String sql,List<Object> paramlist);

    public M exehqlreM(String hql,List<Object> paramlist);
  	
  	public void exesql(String sql,List<Object> paramlist);
  	
  	public List exeHqlrelistTop(String hql,List<String> paramlist,int num);
  	
    public void flush();
    
    public void clear();
    
    public void deleteTable(String sql);
    
    public void addSumplan(String sql);

    public List<M> findpage(String hql,com.hd.microblog.util.PageUtil pageUtil,List<Object> paramlist);

    public List<Map<String, Object>> findpagebysql(String sql,com.hd.microblog.util.PageUtil pageUtil);
    
    public List<Map<String, Object>> findpagebysqls(String sql,com.hd.microblog.util.PageUtil pageUtil,List<Object> paramlist);

}
