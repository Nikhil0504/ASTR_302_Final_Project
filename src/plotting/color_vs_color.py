from astropy.table import Table
import matplotlib.pyplot as plt
from astropy import units as u

# ticks and tick labels
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['ytick.minor.visible'] = True

# show ticks every 0.2 on x and y axis
plt.rcParams['xtick.major.size'] = 4
plt.rcParams['xtick.minor.size'] = 2
plt.rcParams['ytick.major.size'] = 4
plt.rcParams['ytick.minor.size'] = 2

cat = Table.read('../../catalogs/master_catalog_f444w_astropy.cat', format='ascii', delimiter=' ')
# cat = Table.read('/Users/nikhilgaruda/Downloads/G191cats/mastercat.eazycat', format='ascii')
zout = Table.read('../../catalogs/g165_444w_astropy.eazypy.zout.fits', format='fits')

z_phot = zout['z_phot']
mask = (z_phot == -1)

cat = cat[~mask]
zout = zout[~mask]

z_phot = zout['z_phot']


filters = ['F090W', 'F150W', 'F200W', 'F277W', 'F356W', 'F444W']

# convert mjy to AB mag
for filt in filters:
    cat[filt] = (cat[filt].value * u.jansky * 1e-6).to(u.ABmag)

# plot color vs mag 4x2
fig, axes = plt.subplots(4, 2, figsize=(8, 10))
axes = axes.flatten()

# make a custom colormap based on redshift
mask_1 = (z_phot < 0.5)
mask_2 = ((z_phot >= 0.5) & (z_phot < 1.0))
mask_3 = ((z_phot >= 1.0) & (z_phot < 1.5))
mask_4 = ((z_phot >= 1.5) & (z_phot < 2.0))
mask_5 = ((z_phot >= 2.0) & (z_phot < 3))
mask_6 = (z_phot >= 3.)

colors = ['#5904BE', 'blue', '#1CFEFE', 'green', '#FA7228', 'red']

for i in range(6):
    mask = eval(f'mask_{i+1}')
    # axes[0].scatter(cat['F115W'][mask] - cat['F150W'][mask], cat['F090W'][mask] - cat['F115W'][mask], s=0.3, c=colors[i])
    axes[1].scatter(cat['F277W'][mask] - cat['F356W'][mask], cat['F150W'][mask] - cat['F200W'][mask], s=0.3, c=colors[i])
    axes[2].scatter(cat['F356W'][mask] - cat['F444W'][mask], cat['F150W'][mask] - cat['F200W'][mask], s=0.3, c=colors[i])
    axes[3].scatter(cat['F356W'][mask] - cat['F444W'][mask], cat['F200W'][mask] - cat['F277W'][mask], s=0.3, c=colors[i])
    axes[4].scatter(cat['F356W'][mask] - cat['F444W'][mask], cat['F277W'][mask] - cat['F356W'][mask], s=0.3, c=colors[i])
    # axes[5].scatter(cat['F200W'][mask] - cat['F277W'][mask], cat['F115W'][mask] - cat['F150W'][mask], s=0.3, c=colors[i])
    axes[6].scatter(cat['F277W'][mask] - cat['F444W'][mask], cat['F150W'][mask] - cat['F200W'][mask], s=0.3, c=colors[i])
    axes[7].scatter(cat['F277W'][mask] - cat['F444W'][mask], cat['F150W'][mask] - cat['F277W'][mask], s=0.3, c=colors[i])


# set x labels
axes[0].set_xlabel('F115W - F150W')
axes[1].set_xlabel('F277W - F356W')
axes[2].set_xlabel('F356W - F444W')
axes[3].set_xlabel('F356W - F444W')
axes[4].set_xlabel('F356W - F444W')
axes[5].set_xlabel('F200W - F277W')
axes[6].set_xlabel('F277W - F444W')
axes[7].set_xlabel('F277W - F444W')

# set y labels
axes[0].set_ylabel('F090W - F115W')
axes[1].set_ylabel('F150W - F200W')
axes[2].set_ylabel('F150W - F200W')
axes[3].set_ylabel('F200W - F277W')
axes[4].set_ylabel('F277W - F356W')
axes[5].set_ylabel('F115W - F150W')
axes[6].set_ylabel('F150W - F200W')
axes[7].set_ylabel('F150W - F277W')


# set axis limits
axes[0].set_xlim(-0.4, 0.9)
axes[0].set_ylim(-0.4, 1.2)
axes[1].set_xlim(-0.5, 0.5)
axes[1].set_ylim(-0.4, 0.9)
axes[2].set_xlim(-0.5, 0.5)
axes[2].set_ylim(-0.4, 0.8)
axes[3].set_xlim(-0.5, 0.5)
axes[3].set_ylim(-0.6, 0.8)
axes[4].set_xlim(-0.5, 0.6)
axes[4].set_ylim(-0.6, 0.6)
axes[5].set_xlim(-0.7, 0.7)
axes[5].set_ylim(-0.2, 1.)
axes[6].set_xlim(-0.9, 0.6)
axes[6].set_ylim(-0.4, 0.8)
axes[7].set_xlim(-0.9, 0.6)
axes[7].set_ylim(-0.4, 0.8)

# add legend
axes[0].scatter([], [], s=10, c=colors[0], label='z < 0.5')
axes[0].scatter([], [], s=10, c=colors[1], label='0.5 < z < 1.0')
axes[0].scatter([], [], s=10, c=colors[2], label='1.0 < z < 1.5')
axes[0].scatter([], [], s=10, c=colors[3], label='1.5 < z < 2.0')
axes[0].scatter([], [], s=10, c=colors[4], label='2.0 < z < 3.0')
axes[0].scatter([], [], s=10, c=colors[5], label='z > 3.0')

axes[0].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=True)
axes[0].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=True)
axes[0].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=True)
axes[0].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=True)
axes[0].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=True)
axes[0].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=True)


plt.savefig('../../plotting/color_vs_color_f444w_astropy_g191.png', bbox_inches='tight', dpi=300)
plt.show()

