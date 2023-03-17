package com.hd.common.dao.hibernate4;

import java.lang.reflect.Field;
import java.lang.reflect.ParameterizedType;
import java.util.Collection;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import javax.persistence.Id;

import org.hibernate.Criteria;
import org.hibernate.Query;
import org.hibernate.SQLQuery;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.criterion.CriteriaSpecification;
import org.hibernate.criterion.DetachedCriteria;
import org.hibernate.type.Type;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

import com.hd.common.dao.IBaseDao;

/**
 * 
 * @author Victor
 *
 * @version 1.0, 2010-8-12
 */
public abstract class BaseHibernateDao<M extends java.io.Serializable, PK extends java.io.Serializable> implements IBaseDao<M, PK> {

    protected static final Logger LOGGER = LoggerFactory.getLogger(BaseHibernateDao.class);

    private final Class<M> entityClass;
    private final String HQL_LIST_ALL;
    private final String HQL_COUNT_ALL;
    private String pkName = null;

    @SuppressWarnings("unchecked")
    public BaseHibernateDao() {
        this.entityClass = (Class<M>) ((ParameterizedType) getClass().getGenericSuperclass()).getActualTypeArguments()[0];
        Field[] fields = this.entityClass.getDeclaredFields();
        for(Field f : fields) {
            if(f.isAnnotationPresent(Id.class)) {
                this.pkName = f.getName();
            }
        }
        
        //TODO @Entity name not null
        HQL_LIST_ALL = "from " + this.entityClass.getSimpleName() + " order by " + pkName + " asc";
        HQL_COUNT_ALL = " select count(*) from " + this.entityClass.getSimpleName();
    }
        
    @Autowired
    @Qualifier("sessionFactory")
    private SessionFactory sessionFactory;

    public Session getSession() {
        //事务必须是开启的(Required)，否则获取不到
        return sessionFactory.getCurrentSession();
    }
   
    @SuppressWarnings("unchecked")
    @Override
    public PK save(M model) {
        return (PK) getSession().save(model);
    }

    @Override
    public void saveOrUpdate(M model) {
        getSession().saveOrUpdate(model);
    }

    @Override
    public void update(M model) {
        getSession().update(model);

    }

    @Override
    public void merge(M model) {
        getSession().merge(model);
    }

    @Override
    public void delete(PK id) {
        getSession().delete(this.get(id));

    }

    @Override
    public void deleteObject(M model) {
        getSession().delete(model);

    }

    @Override
    public boolean exists(PK id) {
        return get(id) != null;
    }

    @Override
    public M get(PK id) {    	 	
        return (M) getSession().get(this.entityClass, id);
    }

    @Override
    public int countAll() {
    	 Query query = getSession().createQuery(HQL_COUNT_ALL);
        Long total = (Long) query.uniqueResult();
        return total.intValue();
    }

    @Override
    public List<M> listAll() {
    	Query query = getSession().createQuery(HQL_LIST_ALL);
        query.setFirstResult(0);
        List<M> results = query.list();
    	return results;
    } 
    @Override
    public void flush() {
        getSession().flush();
    }

    @Override
    public void clear() {
        getSession().clear();
    }
    
    @Override
    public void deleteTable(String sql){
    	// 执行sql语句 
    	Query query = getSession().createSQLQuery(sql);
    	query.executeUpdate();
    }
    
    @Override
    public void addSumplan(String sql){
    	// 执行sql语句 
    	Query query = getSession().createSQLQuery(sql);
    	query.executeUpdate();
    }
    
    @Override
	public List exesqlrelist(String sql,List<Object> paramlist) {
		// TODO Auto-generated method stub
    	System.out.println("db's sql:");
    	System.out.println(sql);
    	System.out.println("db's paramlist:");
    	System.out.println(paramlist);
		Query query =  getSession().createSQLQuery(sql);
		
		if(paramlist!=null){
			for(int i=0;i<paramlist.size();i++){
				query.setParameter(i, paramlist.get(i));
				
			}
		}
		
		
		return query.setResultTransformer(CriteriaSpecification.ALIAS_TO_ENTITY_MAP).list();
		
	}
	@Override
	public List exehqlrelist(String hql,List<Object> paramlist) {
		// TODO Auto-generated method stub
		Query query =  getSession().createQuery(hql);
		if(paramlist!=null){
		for(int i=0;i<paramlist.size();i++){
			query.setParameter(i, paramlist.get(i)); 
		}
		}
		return query.list();
	}
	
	@Override
	public void exesql(String sql,List<Object> paramlist) {
		// TODO Auto-generated method stub
		Query query =  getSession().createSQLQuery(sql);
		if(paramlist!=null){
		for(int i=0;i<paramlist.size();i++){
			query.setParameter(i, paramlist.get(i)); 
		}
		}
		query.executeUpdate();
	}
	@Override
	public M exesqlreM(String sql, List<Object> paramlist) {
		// TODO Auto-generated method stub
		Query query =  getSession().createQuery(sql);
		if(paramlist!=null){
		for(int i=0;i<paramlist.size();i++){
			query.setParameter(i, paramlist.get(i)); 
		}
		}
		return (M)query.setResultTransformer(CriteriaSpecification.ALIAS_TO_ENTITY_MAP).uniqueResult();
	}

	@Override
	public M exehqlreM(String hql, List<Object> paramlist) {
		// TODO Auto-generated method stub
		Query query =  getSession().createQuery(hql);
		if(paramlist!=null){
		for(int i=0;i<paramlist.size();i++){
			query.setParameter(i, paramlist.get(i)); 
		}
		}
		return (M)query.uniqueResult();
	}
	@Override
	public List exeHqlrelistTop(String hql, List<String> paramlist,int num) {
		Query query =  getSession().createQuery(hql);
		if(paramlist!=null){
		for(int i=0;i<paramlist.size();i++){
			query.setString(i, paramlist.get(i)); 
		}
		}
		query.setFirstResult(0);
		
		query.setFetchSize(num);
		
		return query.list();
	}
	@Override
	public List<M> findpage(String hql,com.hd.microblog.util.PageUtil pageUtil,List<Object> paramlist){
			Query query =  getSession().createQuery(hql).setFirstResult((pageUtil.getPageNo()-1)*pageUtil.getPageSize()).setMaxResults(pageUtil.getPageSize());
			if(paramlist!=null){
				for(int i=0;i<paramlist.size();i++){
					query.setParameter(i, paramlist.get(i)); 
				}
				}
			return query.list();
		}
	public List<Map<String, Object>> findpagebysql(String sql,com.hd.microblog.util.PageUtil pageUtil){
		Query query =  getSession().createSQLQuery(sql).setFirstResult((pageUtil.getPageNo()-1)*pageUtil.getPageSize()).setMaxResults(pageUtil.getPageSize());
		
		return query.setResultTransformer(CriteriaSpecification.ALIAS_TO_ENTITY_MAP).list();
	}
	public List<Map<String, Object>> findpagebysqls(String sql,com.hd.microblog.util.PageUtil pageUtil,List<Object> paramlist){
		Query query =  getSession().createSQLQuery(sql).setFirstResult((pageUtil.getPageNo()-1)*pageUtil.getPageSize()).setMaxResults(pageUtil.getPageSize());
		if(paramlist!=null){
			for(int i=0;i<paramlist.size();i++){
				query.setParameter(i, paramlist.get(i)); 
			}
			}
		return query.setResultTransformer(CriteriaSpecification.ALIAS_TO_ENTITY_MAP).list();
	}
}
