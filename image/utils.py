from image_utils import version, ceph

version.version_string()

# get source store.
src_store = ceph.get_store(conffile_path, ceph_user, keyring_path)
# get dest store.
dst_store = ceph.get_store(conffile_path2, ceph_user, keyring_path2)
# get an image location from source ceph pool.
src_loc = src_store.get_location(pool, image_name)
# copy image from src_store to dst_store, in dst_pool
ceph.copy(src_store, src_loc, dst_store, dst_pool)

##### Example: modify a image.
from image_utils import fish

f = fish.Fish(mon_host, mon_port, client, key, pool, image_name)
f.launch()

f.add_mtu('192.168.1.100', 1450)
f.remove_file('/root/abc.txt')

f.shutdown()
