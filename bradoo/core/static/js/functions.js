function vendors_toggle(source) {
    checkboxes = document.getElementsByName('vendors');
    for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = source.checked;
    }
  }

function products_toggle(source) {
    checkboxes = document.getElementsByName('products');
    for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = source.checked;
    }
  } 