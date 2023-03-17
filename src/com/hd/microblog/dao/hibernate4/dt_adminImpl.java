package com.hd.microblog.dao.hibernate4;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.criterion.CriteriaSpecification;
import org.springframework.stereotype.Repository;

import com.hd.common.dao.hibernate4.BaseHibernateDao;
import com.hd.microblog.dao.dt_adminDao;
import com.hd.microblog.model.dt_admin;

@Repository("dt_adminDao")
public class dt_adminImpl extends BaseHibernateDao<dt_admin, Integer>  implements  dt_adminDao{


	

}
