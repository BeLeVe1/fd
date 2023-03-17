package com.hd.microblog.web.controller.code;

/**
 * 封装所有api请求的返回结果
 */
public class ResultInfo<T> {

	/**
	 * 错误码
	 */
	private int errorCode;
	
	/**
	 * 错误信息
	 */
	private String errorMsg;
	
	/**
	 * 没有错误，返回结果
	 * 有错误，结果为null
	 */
	private T result;
	
	
	public int getErrorCode() {
		return errorCode;
	}
	public void setErrorCode(int errorCode) {
		this.errorCode = errorCode;
	}
	public String getErrorMsg() {
		return errorMsg;
	}
	public void setErrorMsg(String errorMsg) {
		this.errorMsg = errorMsg;
	}
	public T getResult() {
		return result;
	}
	public void setResult(T result) {
		this.result = result;
	}
	
	
	////////////////////////////////////////////////////////////////////
	// 错误1-10是登录错误和其他预留错误
	
	/**
	 * 非法session的错误信息
	 * @return
	 */
	public static ResultInfo<String> getIllegalData() {
		
		ResultInfo<String> info = new ResultInfo<String>();
		info.setErrorCode(10);
		info.setErrorMsg("参数错误！");
		
		return info;
	}
	
}
