package com.hd.microblog.Interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.apache.log4j.Logger;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import com.hd.microblog.model.dt_admin;


/**
 *@Title:
 *@Description:
 *@Author:zhanghl
 *@Since:2015年5月29日
 *@Version:1.1.0
 */
public class AdminCommonInterceptor implements HandlerInterceptor {

	private Logger log = Logger.getLogger(AdminCommonInterceptor.class); 
	
	
    
    public AdminCommonInterceptor() {  
        // TODO Auto-generated constructor stub  
    }  
  
    /** 
     * 在业务处理器处理请求之前被调用 
     * 如果返回false 
     *     从当前的拦截器往回执行所有拦截器的afterCompletion(),再退出拦截器链 
     *  
     * 如果返回true 
     *    执行下一个拦截器,直到所有的拦截器都执行完毕 
     *    再执行被拦截的Controller 
     *    然后进入拦截器链, 
     *    从最后一个拦截器往回执行所有的postHandle() 
     *    接着再从最后一个拦截器往回执行所有的afterCompletion() 
     */  
  
    @Override  
    public boolean preHandle(HttpServletRequest request,  
            HttpServletResponse response, Object handler) throws Exception { 
       	HttpSession session = request.getSession();
    	String url = request.getRequestURL().toString();
    	System.out.println("====="+url);
    	if(url.indexOf("/adminindex") > 0
  				||url.indexOf("/adminwelcome") > 0
  				){
  			dt_admin admin = (dt_admin) session.getAttribute("admin");
  			
  			if((admin == null)){
  				response.sendRedirect("adminlogin");
  				return false;
  			}else{
  				if(admin.getPassword()==null||"".equals(admin.getPassword())){
  					response.sendRedirect("adminlogin");
  					return false;
  				}
  				return true;
  			}
  		}
  		return true;		
      		
    }  
  
    //在业务处理器处理请求执行完成后,生成视图之前执行的动作   
    @Override  
    public void postHandle(HttpServletRequest request,  
            HttpServletResponse response, Object handler,  
            ModelAndView modelAndView) throws Exception {  
        // TODO Auto-generated method stub  
    }  
  
    /*
     * 在DispatcherServlet完全处理完请求后被调用  
     *  
     *   当有拦截器抛出异常时,会从当前拦截器往回执行所有的拦截器的afterCompletion() 
     ***/  
    @Override  
    public void afterCompletion(HttpServletRequest request,  
            HttpServletResponse response, Object handler, Exception ex)  
            throws Exception {  
        // TODO Auto-generated method stub        
    }  
	
	
	
	
	
	
	
}
