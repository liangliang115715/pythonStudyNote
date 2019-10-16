

class Pagenation(object):
    def __init__(self,totalCount,currentPage,perPageNum=30,maxPageNum=7):
        #数据总个数
        self.total_count=totalCount
        #当前页码
        try:
            self.current_page=int(currentPage)
            if self.current_page<= 1:
                self.current_page=1
        except Exception as e:
            self.current_page = 1
        #每页显示数据个数
        self.per_page_item_num=perPageNum
        #最大页数
        self.max_page_num=maxPageNum

    def start(self):
        return (self.current_page-1)*self.per_page_item_num
    def end(self):
        return self.current_page*self.per_page_item_num

    @property
    def num_pages(self):
        a,b=divmod(self.total_count,self.per_page_item_num)
        if a==0:
            return 1
        return a+1
    def page_num_range(self):
        # 总页数小于设置的显示页数
        if self.num_pages<self.max_page_num:
            return range(1,self.num_pages+1)
        #取显示页数的中间数
        part=self.max_page_num//2
        #当前页码小于一半时
        if self.current_page<=part:
            return  range(1,self.max_page_num+1)
        #当前页码+part大于总页数
        if(self.current_page+part)>self.num_pages:
            return range(self.num_pages-self.max_page_num+1,self.num_pages+1)
        #一般情况
        return range(self.current_page-part,self.current_page+part+1)

    def page_str(self):
        page_lsit=[]
        first="<a href='index2.html?p=%s'>首页</a>" % (1)
        page_lsit.append(first)
        if self.current_page==1:
            prev="<a href='#'>上一页</a>"
        else:
            prev = "<a href='index2.html?p=%s'>上一页</a>" % (self.current_page-1,)
        page_lsit.append(prev)
        for i in self.page_num_range():
            if i == self.current_page:
                temp="<a href='index2.html?p=%s' style='color:red;'>%s</a>"%(i,i,)
            else:
                temp="<a href='index2.html?p=%s'>%s</a>"%(i,i,)
            page_lsit.append(temp)
        if self.current_page==self.num_pages:
            prev="<a href='#'>下一页</a>"
        else:
            prev = "<a href='index2.html?p=%s'>下一页</a>" % (self.current_page+1,)

        page_lsit.append(prev)
        end="<a href='index2.html?p=%s'>尾页</a>" % (self.num_pages,)
        page_lsit.append(end)

        return "".join(page_lsit)
