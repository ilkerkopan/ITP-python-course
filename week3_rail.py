rail_length=310
l_size=100
m_size=30
s_size=10

l_size_count=rail_length//l_size
m_size_count=(rail_length-(l_size_count*l_size)) // m_size
s_size_count=(rail_length-(l_size_count*l_size)-(m_size_count*m_size)) // s_size

print("number of 100 meter rails:"+str(l_size_count))
print("number of 30 meter rails:"+str(m_size_count))
print("number of 10 meter rails:"+str(s_size_count))