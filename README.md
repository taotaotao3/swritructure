# swritructure

Name:swritructure
Explanation:Please use it when you want to know target program structure.

License:MIT
Using method:  
pip install swritructure

>python swritructure.py (target program start file name)

ex:
import swritructure as sw

sw.swritructure_main('your_program.py')


Result:exporting swritructure.txt



--swritructure.txt---

 aaaaaa.py
     |

    ∟createData.py

    |   |

    |   getTopURLStatus()

    |    |  　|

    |    |    ∟formatHTMLText.py

    |    |  　|          |

    |    |    |          formatHtml()

    |    |  　|

    |    |    ∟bs4.py

    |    |  　|          |

    |    |    |          BeautifulSoup()

    |    |  　|

    |    |    ∟checkTorihikiginkou.py

    |    |  　|          |

    |    |    |          checkTorihikiginkou()
