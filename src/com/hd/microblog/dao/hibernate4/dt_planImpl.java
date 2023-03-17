package com.hd.microblog.dao.hibernate4;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.criterion.CriteriaSpecification;
import org.springframework.stereotype.Repository;

import com.hd.common.dao.hibernate4.BaseHibernateDao;
import com.hd.microblog.dao.dt_planDao;
import com.hd.microblog.model.dt_plan;

@Repository("dt_planDao")
public class dt_planImpl extends BaseHibernateDao<dt_plan, Integer>  implements  dt_planDao{


	

}
