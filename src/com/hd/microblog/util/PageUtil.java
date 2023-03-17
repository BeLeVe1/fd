package com.hd.microblog.util;

import java.util.List;

public class PageUtil {

	private int totalRecords; // 总条数
	private int pageSize =25; // 一页显示多少条
	private int pageNo;// 当前页

	private int totalPages;// 总页数
	private List<?> list;

	public List<?> getList() {
		return list;
	}

	public void setList(List<?> list) {
		this.list = list;
	}

	public int getTotalRecords() {
		return totalRecords;
	}

	public void setTotalRecords(int totalRecords) {
		this.totalRecords = totalRecords;
	}

	public int getPageSize() {
		return pageSize;
	}

	public void setPageSize(int pageSize) {
		this.pageSize = pageSize;
	}

	public int getPageNo() {
		if (this.pageNo == 0)
			this.pageNo = 1;
		return pageNo;
	}

	public void setPageNo(int pageNo) {
		this.pageNo = pageNo;
	}

	public int getTotalPages() {
		int i = this.totalRecords / this.pageSize;
		if ((this.totalRecords % this.pageSize) < this.pageSize) {
			i = i + 1;
		}

		return i;
	}

}
